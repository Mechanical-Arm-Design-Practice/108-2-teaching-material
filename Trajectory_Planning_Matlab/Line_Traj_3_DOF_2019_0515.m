function Line_Traj_3_DOF()
    %% ��l�]�w
    clear;clc;%clf;
    %% parameter for robot manipulator hardware
    DOF = 3; 
    Link            = [  10 30 30 ];    % �]�w�s�����
    Parameter.Gear  = [  110 105 80 ];  % �U�b��t��   
  
  %% parameter for trajectory planning  
    Current.Pos = [ -20 10 0 ];         % �_�l��m
    Goal.Pos    = [  20 40 20 ];        % �ؼЦ�m
    
    Vel.Start   = 0                     % �_�l�t�� ( cm/s )
    Vel.Drv     = 50;                   % �̤j�X�ʳt�� ( cm/s )
    Vel.Acc     = 100;                  % �[�t�� ( cm/s2 )
    Vel.Tick    = 0.04 ;                % Sample Time 
    max_mov_dis = Vel.Drv * Vel.Tick
    
    Error  = norm( Goal.Pos - Current.Pos );
    Vector = ( Goal.Pos - Current.Pos ) / Error;
    
   %% parameter for �������A��(FSM) 
    Vel.State   = 'VEL_IDEL';   % ��l���A
    Vel.Now     = 0;            % ��e�t��
    Vel.Dis     = 0;            % �ثe�]���Z��
    %�̤j�t�׮ɪ����ʶq   50(cm/s)*0.05(s) = 2.5 cm/sample_time
    
     %% �B�ʾǭp��
    Current.Angle = IK(Current.Pos, Link);
    Info = FK(DOF, Current.Angle, Link);
    
    Goal.Angle = IK(Goal.Pos, Link);
    Info  = FK(DOF, Goal.Angle, Link);
    
    Path    = Current;
    %% for record
    Past_RPM = zeros(1,3);
    MotorACC = zeros(1,3);
    
    Rec_P   = Path.Pos';
    Rec_ErrP= Path.Pos;
    Rec_V   = 0;
    Rec_DD  = 0;
    Rec_Ang = Path.Angle';
    Rec_RPM = zeros(3,1);
    Rec_Acc = zeros(3,1  );
    %% Process
    while( abs(Error) > 0.0001 )
%         
        % Ū���U�b�ثe�^�¨íp��ثe��m
        Feedback_Ang = Path.Angle;                      
        Info  = FK(DOF, Feedback_Ang, Link);   
        
        DrawRobotManipulator( DOF, Info.JointPos, Info.JointDir, 1 , [-145 30 ] );
        title('RRR Manipulator');
        
        % �ھڥثe�t�פλ~�t ��s�U�@��t�פβ��ʶq
        Vel = CalculateMovementDistance( Vel, Error );
        
        % ��s���|�W���U�@���m(�u�@�Ŷ��y��W��(17/20))
        Path.Pos   = Path.Pos + Vector * Vel.Dis;
        
        % ��s�U���`�����t��(�u�@�Ŷ��y��W��(18/20))
        Path.Angle = IK(Path.Pos, Link);
        Ang_V  = (Path.Angle - Feedback_Ang)*pi/180 /  Vel.Tick;
        
        % �N���t���ন RPM(�u�@�Ŷ��y��W��(18/20))
        RPM    = 60*Ang_V/(2*pi)
        
        % ��s�P�ؼЦ�m���~�t
        Error  = norm( Goal.Pos - Path.Pos );
   
        pause( Vel.Tick );
        
        % record1
        MotorACC = ( Ang_V .* Parameter.Gear - Past_RPM ) ./ Vel.Tick ;
        Past_RPM =   Ang_V .* Parameter.Gear;
        Rec_P   = [ Rec_P   Info.Pos ];
        Rec_V    = [ Rec_V    Vel.Now ];
        Rec_Ang = [ Rec_Ang  Path.Angle'];
        Rec_RPM = [ Rec_RPM  RPM' ] ;
        Rec_Acc = [ Rec_Acc  MotorACC' ];
    end
    
    % record2
    Rec_P   = [ Rec_P   Path.Pos' ];
    Rec_Ang = [ Rec_Ang  Path.Angle'];
    
    Rec_V   = [ Rec_V    0 ];
    Rec_RPM = [ Rec_RPM  zeros(3,1) ] ;
    Rec_Acc = [ Rec_Acc  zeros(3,1) ];
    
    %% Draw Trajectory
    figure(1)
    plot3(  Rec_P(1,:), Rec_P(2,:), Rec_P(3,:) ,'bo');
    
    t  =  ( 1:size(Rec_V,2) ) * Vel.Tick;
    figure(2)
    plot(  t , Rec_V ,'-bo');
    axis( [ min(t) max(t) min(Rec_V) max(Rec_V) + 2] )
    
    
%     DrawAngle( t , Rec_Ang );
    DrawRPM( t , Rec_RPM );
%     DrawACC( t, Rec_Acc );
    
end

%% ���A�� %%%%%%%%%%%%%%%%%%%
function Vel = CalculateMovementDistance( Vel , Error )
    Vel.Dis = 0;
    
    if( strcmp( Vel.State, 'VEL_IDEL' ) )
         Vel.Now   =  0; 
         Vel.State = 'VEL_ACC';
         Vel.Dis = Vel.Now * Vel.Tick;
     
    elseif( strcmp( Vel.State, 'VEL_ACC' ) )
        tmp = Vel.Now;
		Vel.Now = tmp + (Vel.Acc * Vel.Tick);
        Vel.Dis = (tmp + Vel.Now)*Vel.Tick*0.5;
        
		if ( Vel.Now >= Vel.Drv )
			Vel.Now	  = Vel.Drv;
			Vel.State = 'VEL_KEEP';
            Vel.Dis = tmp * Vel.Tick + (Vel.Tick*(Vel.Now-tmp))/2;
        end
        
    elseif( strcmp( Vel.State, 'VEL_KEEP' ) )
        [IsDec Vel] = IsDeceleration( Vel, Error );
        
        if ( IsDec == 0 )
            Vel.Now = Vel.Drv;
            Vel.Dis = Vel.Now *  Vel.Tick;
        else
            Vel.State = 'VEL_DEC';
        end
        
    elseif( strcmp( Vel.State, 'VEL_DEC' ) )
        Vel.Now = Vel.Now - Vel.Acc * Vel.Tick;

		if ( Vel.Now <= Vel.Start )
			Vel.Now   = Vel.Start;
			%Vel.Dis   = Vel.Now * Vel.Tick;
% 			Vel.State = 'VEL_REMAIN';
        end
		Vel.Dis   = Vel.Now * Vel.Tick + ( Vel.Acc * Vel.Tick^2 )/2.0;
        
    else
        fprintf('err')
    end

	if ( Vel.Dis >= abs(Error) )
		Vel.Dis = abs(Error);
    end
    
	if ( Error < 0 )
		Vel.Dis =  -1.0 * Vel.Dis;
    end

end
%% ��γt�צ��u %%%%%%%%%%%%%%%
function [isDec Vel] = IsDeceleration( Vel , Error )
    % �q�ثe�t�ר찱��һݪ���t�ɶ�
	T  = (( Vel.Now - Vel.Start ) / Vel.Acc );

    % �ھڴ�t�ɶ����� �q�ثe�t�ר찱�� �һݭn����t�Z��
	d1 = ( Vel.Now * T ) / 2.0;
    d2 = Vel.Start * T;
   
    % �Y�ثe�Z���~�t�p�� ��t�Z�� �h�^�Ǵ�t�T��
	if ( abs(Error) <= d1+d2 )
        t1      = ( abs(Error) - d1  ) /  Vel.Now;
        t2      = Vel.Tick - t1;
        

        
        tmp = Vel.Now;
        Vel.Now = tmp - Vel.Acc * t2;
        Vel.Dis = Vel.Now * Vel.Tick + 0.5*abs(tmp-Vel.Now)*Vel.Tick;
		isDec = 1;
	else
		isDec = 0;
    end
end
%% ���B�ʾ�FK
function Info = FK(DOF, Angle, Link)
    %  �׫׶q�� �y�׶q
    Angle = Angle*pi/180;
    
    % ================ Step1 �t�m���u�y�Шt ================  
    % (1) �M�w������u�U���`��0�ת����A
    % (2) �M�w�U���`�y�Шt��Z�b
    % (3) �w�q�U���`��XY�b 
    % (4) �̫�Хܥ����I���y�Шta,s,n
      
    % ================ Step2 �إߢҢְѼƳs��� ================  
    % �@��ai�B�\i�Bdi�B�ci�|�ӰѼ�
    % ��i : distance(zi-1, zi) along xi
    % �\i : angle(zi-1, zi) about xi
    % ��i : distance(oi-1,xi) along zi-1
    % �ci : angle(xi-1, xi) about zi
    %
    %                   �Ң� Parameter Table
    %+---+-----------+-----------+-----------+-----------+
    %| j |        �� |     alpha |        �� |     theta |
    %+---+-----------+-----------+-----------+-----------+
    %| 1 |          0|         90|        ��1|         90|
    %| 2 |        ��1|          0|          0|          0|
    %| 3 |        ��2|          0|          0|          0|
    %+---+-----------+-----------+-----------+-----------+
    %
    % RRR��DH�s��Ѽ� [  ��      �\    �@��      �@�c   ]
    DHParameter  =  [   0     pi/2   Link(1)     pi/2;      
                      Link(2)      0      0        0;       
                      Link(3)      0      0        0   ];   
                    
    %================ Step3 �p��Ңֻ����ഫ�x�} ================   
    % ��l�]�w
    JointPos = [0 ;0 ;0];
    JointDir = [1 0 0; 0 1 0; 0 0 1];
    T0_3 = [ 1 0 0 0; 0 1 0 0;0 0 1 0; 0 0 0 1];    
    
    % �p��A1, A2, A3
    for i = 1 : DOF
        A =  GenerateTransformationMatrices( Angle(i), DHParameter(i,:));
        T0_3 = T0_3 * A;
        JointPos = [ JointPos T0_3( 1:3, 4)];    % �x�s���`���y�Ц�m�A�x�s�����I����m O0_6 (O0_6��1*3�x�}) 
        JointDir = [ JointDir T0_3( 1:3, 1:3 ) ];
    end
    
    Info.Pos = JointPos(1:3,4);
    Info.JointPos = JointPos;
    Info.JointDir = JointDir;
    
end

%% �Ңֻ����ഫ�x�}
function A =  GenerateTransformationMatrices( Theta, DH_Parameter ) 
    %   �̧ǥN�J �ثe�U�b������, �̧ǥN�J �U�C(�b)���s��Ѽƪ�  Ex:�Ĥ@�b, �Ĥ@�C
    %   �̧ǭp�� T0_1~T5_6 = A1~A6 
    %   DH_Parameter (1) = ��
    %   DH_Parameter (2) = �\      
    %   DH_Parameter (3) = ��       
    %   DH_Parameter (4) = �c
                                                                                                       
    C_Theta = cos( Theta + DH_Parameter(4) );
    S_Theta = sin( Theta + DH_Parameter(4) );
    C_Alpha = cos( DH_Parameter(2) );
    S_Alpha = sin( DH_Parameter(2) ); 
    
    A = [   C_Theta   -1*S_Theta*C_Alpha        S_Theta*S_Alpha     DH_Parameter(1) * C_Theta; 
            S_Theta      C_Theta*C_Alpha     -1*C_Theta*S_Alpha     DH_Parameter(1) * S_Theta;
            0                    S_Alpha                C_Alpha                DH_Parameter(3);     %%%%%%%%%%%
            0                          0                      0                             1   ];
end

%% �f�B�ʾ�IK
function Angle = IK(Goal, Link)

    % �Ĥ@�b���F���� theta1
    Angle(1) = -atan2(Goal(1), Goal(2)); 
  
    % �ĤT�b���F���� theta3
    cosTheta3     = ((Goal(3)- Link(1))^2  +  Goal(1)^2  +  Goal(2)^2 - (Link(2)^2+Link(3)^2)) / (2.0 *Link(2)*Link(3));
    c3 = cosTheta3;
    Angle(3) = atan2( -1*sqrt(1-c3^2),c3 );
     
    % �ĤG�b���F���� theta2
    r = sqrt(Goal(1)^2+Goal(2)^2);
    Theta3 =Angle(3);
    Angle(2) = atan2(Goal(3)-Link(1),r)-...
    atan2(Link(3)*sin(Theta3), Link(2)+Link(3)*cos(Theta3));   

     % �y�׶q �� �׫׶q
    Angle = Angle*180/pi;
end

%%  �e�� �e������u ��J: �ۥѫסA�U���`����m�A�U���`���y��
function DrawRobotManipulator( DOF, JointPos, JointDir , FigNum , View )

    figure(FigNum)

    hold off
    plot3( JointPos(1,1:end), JointPos(2,1:end), JointPos(3,1:end),'linewidth', 4)
    hold on
    plot3( JointPos(1,1:end), JointPos(2,1:end), JointPos(3,1:end),'ro','linewidth', 7);

    grid on
    xlabel('X�b');
    ylabel('Y�b');
    zlabel('Z�b');
    X =10;
    Y =10;
    Z =20;
    %-------------------------------------
    BaseX = [X X -X -X X];
    BaseY = [Y -Y -Y Y Y];
    BaseZ = [0 0 0 0 0];
    patch(BaseX,BaseY,BaseZ,'k')
    %-------------------------------------
    BaseX = [X X X X X];
    BaseY = [Y -Y -Y Y Y];
    BaseZ = [0 0 -Z -Z 0];
    patch(BaseX,BaseY,BaseZ,'k')
    %-------------------------------------
    BaseX = [X -X -X X X];
    BaseY = [Y Y Y Y Y];
    BaseZ = [0 0 -Z -Z 0];
    patch(BaseX,BaseY,BaseZ,'k')
    %-------------------------------------
    BaseX = [-X -X -X -X -X];
    BaseY = [-Y Y Y -Y -Y];
    BaseZ = [0 0 -Z -Z 0];
    patch(BaseX,BaseY,BaseZ,'k')
    %-------------------------------------
    BaseX = [X -X -X X X];
    BaseY = [-Y -Y -Y -Y -Y];
    BaseZ = [0 0 -Z -Z 0];
    patch(BaseX,BaseY,BaseZ,'k')

    for i = 1 : DOF+1

        %-----------------------------------------
        nUnit_v = JointPos( : , i ) + 5 * JointDir( : , 3 * (i-1) + 1 );        % normal ����V�q 
        nBase   = [JointPos( : , i ) nUnit_v];
        plot3(nBase(1,1:end),nBase(2,1:end),nBase(3,1:end),'y','linewidth',2);  
        %--------------------------------------------
        sUnit_v = JointPos( : , i ) + 5 * JointDir( : , 3 * (i-1) + 2 );        % sliding �ưʦV�q
        sBase   = [JointPos( : , i ) sUnit_v];
        plot3(sBase(1,1:end),sBase(2,1:end),sBase(3,1:end),'g','linewidth',2);
        %--------------------------------------------
        aUnit_v = JointPos( : , i ) + 5 * JointDir( : , 3 * (i-1) + 3 );        % approach �a��
        aBase   = [JointPos( : , i ) aUnit_v];
        plot3(aBase(1,1:end),aBase(2,1:end),aBase(3,1:end),'r','linewidth',2);
        %--------------------------------------------
        hold on
    end
    view( View )
    %axis equal
    axis( [-50 50 -30 80 -20 80])
end

%%
function DrawAngle( t, Rec_Ang )
figure(3)
subplot(3,1,1)
plot( t, Rec_Ang(1,:));
title('\theta1'); xlabel('Sec'); ylabel('degree'); grid on
subplot(3,1,2)
plot(t, Rec_Ang(2,:));
title('\theta2'); xlabel('Sec'); ylabel('degree'); grid on
subplot(3,1,3)
plot(t, Rec_Ang(3,:));
title('\theta3'); xlabel('Sec'); ylabel('degree'); grid on

end

function DrawRPM( t, Rec_RPM )
figure(4)
subplot(3,1,1)
plot(t, Rec_RPM(1,:),'-bo');
title('\theta1'); xlabel('Sec'); ylabel('RPM'); grid on
subplot(3,1,2)
plot(t, Rec_RPM(2,:),'-bo');
title('\theta2'); xlabel('Sec'); ylabel('RPM'); grid on
subplot(3,1,3)
plot(t, Rec_RPM(3,:),'-bo');
title('\theta3'); xlabel('Sec'); ylabel('RPM'); grid on

end

function DrawACC( t, Rec_ACC )
figure(5)
subplot(3,1,1)
plot(t, Rec_ACC(1,:) ,'-bo');
title('\theta1'); xlabel('Sec'); ylabel('Acc'); grid on
subplot(3,1,2)
plot(t, Rec_ACC(2,:) ,'-bo');
title('\theta2'); xlabel('Sec'); ylabel('Acc'); grid on
subplot(3,1,3)
plot(t, Rec_ACC(3,:) ,'-bo');
title('\theta3'); xlabel('Sec'); ylabel('Acc'); grid on

end
