function main()
    clc
    clear
    close all

    Joint_Pos = [];
    Goal      = [30.5 12.2 ]
    Joint_Ang = [60 -30];
    Link      = [30 20];
    
    % Inverse Kinematic
    figure(2);
    Joint_Ang = TwoLink_IK(Goal, Link);
    Joint_Pos = TwoLink_FK(Joint_Ang, Link);
    Draw_TwoLink_Manipulator(Joint_Pos, '-ro');
    title('Inverse Kinematic');

end

function Joint_Ang = TwoLink_IK(Goal, Link)
    Beta  = atan2(Goal(2), Goal(1));
    Joint_Ang(2) = -acos( (Goal(1)^2 + Goal(2)^2 - Link(1)^2 - Link(2)^2)/...
                         (2*Link(1)*Link(2)))
                     
    a = Link(2)*sin(Joint_Ang(2))
    b = Link(1) + Link(2)*cos(Joint_Ang(2))
    Alpha = atan2(a,b);
    
    Joint_Ang(1) = (Beta-Alpha)  
    Joint_Ang = Joint_Ang*180/pi%%徑度轉角度
end

function Joint_Pos = TwoLink_FK(Joint_Ang, Link)

    Joint_Ang = Joint_Ang*pi/180;%%角度轉徑度
    orig  = [0 0];
    elbow = [0 0];
    goal  = [0 0];

    elbow(1) = Link(1)*cos(Joint_Ang(1));
    elbow(2) = Link(1)*sin(Joint_Ang(1));

    goal(1) = Link(1)*cos(Joint_Ang(1)) + Link(2)*cos(Joint_Ang(1)+Joint_Ang(2));
    goal(2) = Link(1)*sin(Joint_Ang(1)) + Link(2)*sin(Joint_Ang(1)+Joint_Ang(2));

    Joint_Pos = [orig ; elbow ; goal];
end

function Draw_TwoLink_Manipulator(Joint_Pos, type)
    plot(Joint_Pos(:,1),Joint_Pos(:,2),type,'linewidth',3);
    axis([-10 50 -10 50]);

    rectangle('Curvature', [0 0], 'Position', [-10 -10 20 10], 'EdgeColor', 'k',...
    'FaceColor', 'k', 'LineWidth', 2); 
    % Curvature曲率 Position位置 EdgeColor邊框顏色 FaceColor表面顏色
end


