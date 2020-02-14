function Trajectory_Trapezoidal_4()

%%
    clear;
    clc;
    close all;
    %% input condition
    Spd = 0.2;
    qi = [  0;     0;     0;     0;     0;     0; 0];                   % �_�l����
    qf = [ 59;    50;   104;    29;   -104;   20;  36];                 % ���I����
    V_Lim = [ 20;    25;    30;    15;    30;   20 ; 12]*360/60*Spd;    % �U�b�����t��
    A_Lim = [ 20;  12.5;    60;   7.5;    60;   20 ; 20]*360/60*Spd;    % �U�b�����[�t��
    %% Parameter setting
    N  = size(qi, 1);       % �b��
    h  = abs(qf - qi);      % �U�b����ʪ�����
    global tick;
    tick  = 0.05;
    sync_flag = 1;          % enable or disable sync traj
    
    Vv = V_Lim;             % ��l�ƦU�b�B�઺�t�שR�O
    Aa = A_Lim;             % ��l�ƦU�b�B�઺�[�t�שR�O
    Ta = zeros(N, 1);       % �U�b�[�t�ɶ�
    T  = zeros(N, 1);       % �U�b���ʮɶ�
    
    %% �p��U�b��T�èM�w�D�b
    for i = 1 : size(qi, 1)
        if( h(i) >= (Vv(i)^2) / Aa(i))                       %������γt�ױ���
            % �p��U�b��T_Max,  Ta_Max, �t�שM�[�t�� 
            T(i)  = (h(i)*Aa(i) + Vv(i)^2) / (Aa(i)*Vv(i));
            T(i)  = ceil(T(i) / tick) * tick;
            Ta(i) = Vv(i) / Aa(i);
            Ta(i) = ceil(Ta(i) / tick) * tick;
        else
            % �p���T_Max,  Ta_Max, �t�שM�[�t�� 
            Ta(i) = sqrt(h(i)/Aa(i));               
            Ta(i) = ceil(Ta(i) / tick) * tick;
            Aa(i) = h(i) / (Ta(i)^2);
            T(i)  = 2 * Ta(i);
            Vv(i) = Aa(i) * Ta(i);
        end
    end
    ti          = 0;            % �_�l�ɶ�
    [T_Max Idx] = max(T);       % �D�b�����ʮɶ��P�D�bID
    tf          = T_Max;        % �D�b�����I�ɶ�
    Ta_Max      = Ta(Idx);      % �D�b���[�t�ɶ�
    h_Main      = h(Idx);       % �D�b����ʨ���
    A_Main      = Aa(Idx);      % �D�b�[�t��
    V_Main      = Vv(Idx);      % �D�b�t��
    
   
    %% ��s�U�b���t�׻P�[�t�סA���ˬd�O�_�W�X�ۨ�����
    for i = 1 : N
        % �q�b�t�X�D�b(T_Max�PTa_Max)�A��s��t�׻P�[�t��
        Slave_New_V = h(i) ./ (T_Max - Ta_Max);
        Slave_New_A = h(i) ./ (Ta_Max .* (T_Max - Ta_Max));
        
        % ��s�᪺�[�t�פj��쥻���[�t�� (�D�b�[�t�ɶ��L��(�j��Y�@�q�b))
        if( Slave_New_A > Aa(i))
            %��s T_Max �P Ta_Max
            Ta_New1 = (h(i) / Aa(i)) * (V_Main / h_Main);
            Ta_New1 = ceil(Ta_New1 / tick) * tick;
            T_New1  = h_Main / V_Main + Ta_New1;
            T_New1  = ceil(T_New1 / tick) * tick;
            Ta_Max  = Ta_New1;
            T_Max   = T_New1;   
            
            % ��ӱq�b�����סB�t�׻P�[�t�� ��s���D�b(�D�b���H��)
            h_Main  = h(i);
            V_Main  = h(i) ./ (T_Max - Ta_Max);
            A_Main  = h(i) ./ (Ta_Max .* (T_Max - Ta_Max));
            
        % ��s�᪺�t�פj��쥻���t�� �D�b�[�t�ɶ��L�u(�p��Y�@�q�b)
            % ��s T_Max �P Ta_Max
        elseif(Slave_New_V > Vv(i))
            %��s T_Max �P Ta_Max
            Ta_New2 = (h_Main / A_Main) * (Vv(i) / h(i));
            Ta_New2 = ceil(Ta_New2 / tick) * tick;
            T_New2  = h(i) / Vv(i) + Ta_New2;
            T_New2  = ceil(T_New2 / tick) * tick;
            Ta_Max  = Ta_New2;
            T_Max   = T_New2;
            
            % ��ӱq�b�����סB�t�׻P�[�t�� ��s���D�b(�D�b���H��)
            h_Main  = h(i);
            V_Main  = h(i) ./ (T_Max - Ta_Max);
            A_Main  = h(i) ./ (Ta_Max .* (T_Max - Ta_Max));
        end
    end
   
    % ---------------------------
    Vv = h' ./ (T_Max - Ta_Max)
    Aa = h' ./ (Ta_Max .* (T_Max - Ta_Max))
    Dis = Vv .* (T_Max - Ta_Max)
    % ---------------------------
    
    % ===============���W���X���t�׻P�[�t�שҶ]���Z��==================
    for i=1:N
        if(Vv(i) > V_Lim(i))
            Vv(i) = V_Lim(i);
        end
        if(Aa(i) > A_Lim(i))
            Aa(i) = A_Lim(i);
        end
    end
    Up   = T_Max - Ta_Max*2;
    Down = T_Max;
    H    = Vv;
    Dis  = (Up+Down)*H / 2.0;  
    Vv;
    cf = [Dis ;qf'];
    % ===============================================================
    
    % ======= �P�_�O�_�n�}�ҳt�צP�B =======
    if(sync_flag)
        tf = T_Max;
    else
        Vv = V_Lim;
        Aa = A_Lim;
    end
    % =====================================
    All_Joint_Q_traj = [];
    All_Joint_V_traj = [];
    All_Joint_A_traj = [];
    for i = 1 : size(qi, 1)
        % ���ͦ�m�B�t�׻P�[�t�ת����u���
        if(sync_flag)
            [Q, V, A] = Trapezoidal_Curve(qi(i), qf(i), ti, T_Max, Ta_Max, Vv(i), Aa(i));
        else
            [Q, V, A] = Trapezoidal_Curve(qi(i), qf(i), ti, T(i), Ta(i), Vv(i), Aa(i));
        end
        
        TT = T(i);
             %% ---- �e�Ϫ����� begin ---
             
        t  = ti : tick : T(i);
        t  = [ti-0.01, ti, t, T(i), T(i)+0.01];
        t  = ti : tick : tf;
        t  = [ti-0.01, ti, t, tf, tf+0.01];
        
        tmp_Q = [ 0, 0,  Q,  Q(end)*ones(1,(length(t)-length(Q)-2))  ];
        tmp_V = [ 0, 0,  V,  V(end)*ones(1,(length(t)-length(V)-2))  ];
        tmp_A = [ 0, 0,  A,  A(end)*zeros(1,(length(t)-length(A)-2)) ];
        
        All_Joint_Q_traj = [All_Joint_Q_traj ;tmp_Q];
        All_Joint_V_traj = [All_Joint_V_traj ;tmp_V];
        All_Joint_A_traj = [All_Joint_A_traj ;tmp_A];
    end
    PlotResult(1, t , All_Joint_Q_traj , 'Position', 'rad', '[s]');  
    PlotResult(2, t , All_Joint_V_traj , 'Velocity', 'deg/s', '[s]' );
    PlotResult(3, t , All_Joint_A_traj , 'Acceleration', 'deg/s^2', '[s]' );
    

function SaveData(filename, Data)
    fid=fopen(filename,'w');
    fprintf(fid,' %g ',Data);
    fclose(fid);  
 
   
function PlotResult(No, t, Data, Title, yLabel, xLabel )
    figure(No)
    plot(t , Data(1, 1:end), '-r');  hold on
    plot(t , Data(2, 1:end), '--g'); 
    plot(t , Data(3, 1:end), '.-b'); 
    plot(t , Data(4, 1:end), '+-c');  
    plot(t , Data(5, 1:end), ':m');  
    plot(t , Data(6, 1:end), 'x-k'); 
    plot(t , Data(7, 1:end), 'x-c'); 
    hold off
    legend('J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7');
    title(Title), ylabel(yLabel), xlabel(xLabel)
    Q1_Max = max(max(Data)) + (max(max(Data)) - min(min(Data))) * 0.1;
    Q1_Min = min(min(Data)) - (max(max(Data)) - min(min(Data))) * 0.1;
    axis([min(t), max(t), Q1_Min, Q1_Max])    
    
function [QQ, VV, AA] = Trapezoidal_Curve(qi, qf, ti, tf, Ta, Vv, Aa)
    global tick;
    Vv = sign(qf - qi) * Vv;
    Aa = sign(qf - qi) * Aa;
    
    QQ = []; VV = []; AA = [];
    for t = ti : tick : tf
        % �קK�p���I����ǫ׿��~�A�ӳy���~�P
        % ex. �i��|�o�� 10.000 > 10 �o�ر��p 
        if(roundn(t, -4) < roundn(ti+Ta, -4)) 
            qt = qi + 0.5 * Aa * (t - ti)^2;
            vt = Aa * (t - ti);
            at = Aa;
        elseif(roundn(ti+Ta, -4) <= roundn(t, -4) && roundn(t, -4) < roundn(tf-Ta, -4))
            qt = qi + Aa * Ta * (t - ti - Ta/2);
            vt = Vv;
            at = 0;
        else
            qt = qf - 0.5 * Aa * (tf - t)^2;
            vt = Aa * (tf - t);
            at = -Aa;
        end
        QQ  = [QQ qt];
        VV  = [VV vt] ;
        AA  = [AA at] ;
    end
