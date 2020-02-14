function main()
    clf;
    fram = 200;
    for i= 1:1:fram
        Aorg = [0 0 0]'; %�_�l�I�y�Ф���
        AorgVecxyz = [1 0 0; 0 1 0; 0 0 1]'; %�_�l�I�U�b�V�q

        AtmpVxyz = [];
        for j= 1:1:3
            AtmpVxyz = [AtmpVxyz HomoRot('z',180*i/fram)*HomoRot('y',90*i/fram)*HomoRot('x',90*i/fram)*([AorgVecxyz(:,j) ;1])] %�U�b�P�ɱ���V�q(�i�ۦ���ηs�W����)%���׬����
        end
        AendVecxyz = AtmpVxyz;
        
        Atmp =  HomoTra(1*i/fram,0*i/fram,0*i/fram)*[Aorg; 1];%�Ȧs���I�y�Ф��ߦ첾(�i�ۦ���첾) %�y�ЦV�q1�����
        
        Aend = Atmp(1:3,:);%���I�y�Ф���
        Ax = [Aend(1)+AendVecxyz(1,1) Aend(2)+AendVecxyz(2,1) Aend(3)+AendVecxyz(3,1)];%���I�y�Ф�x�b�����I
        Ay = [Aend(1)+AendVecxyz(1,2) Aend(2)+AendVecxyz(2,2) Aend(3)+AendVecxyz(3,2)];%���I�y�Ф�y�b�����I
        Az = [Aend(1)+AendVecxyz(1,3) Aend(2)+AendVecxyz(2,3) Aend(3)+AendVecxyz(3,3)];%���I�y�Ф�z�b�����I
    
        plot3([Aend(1) Ax(1)],[Aend(2) Ax(2)],[Aend(3) Ax(3)],'r-o'); %�e�Xx�b�A�è�s�e��
        hold on
        plot3([Aend(1) Ay(1)],[Aend(2) Ay(2)],[Aend(3) Ay(3)],'g-o'); %�e�Xy�b�A�è�s�e��
        hold on
        plot3([Aend(1) Az(1)],[Aend(2) Az(2)],[Aend(3) Az(3)],'b-o'); %�e�Xz�b�A�è�s�e��
        hold off
        axis([-5 5 -5 5 -5 5]);grid on; %�]�w�ɭ�
        
        drawnow 
    end
%% �m��2 p.14
    Aorg = [7, 3, 2]'
    %Ans = HomoTra(4,-3,7)*HomoRot('y',90)*HomoRot('z',90)*[Aorg; 1]
    Ans = HomoRot('z',90)*[Aorg; 1];
    A = HomoRot('z',90)
%% �d��2 p.16
   B = HomoTra(0,1,1)*HomoTra(-0.6,0.4,0)*HomoTra(0.1,0.1,2)*HomoRot('x',180)*HomoRot('z',-90)

end


function Tra = HomoTra(x,y,z) % �����y�Х����ഫ�x�}
    Tra = [1 0 0 x; 0 1 0 y; 0 0 1 z; 0 0 0 1];
end

function Rot = HomoRot(xyz,Deg) % �����y�б����ഫ�x�}
    Deg = Deg*pi/180;
    switch(xyz)
        case 'x'
            Rot = [1 0 0 0; 0 cos(Deg) -sin(Deg) 0; 0 sin(Deg) cos(Deg) 0; 0 0 0 1];
        case 'y'
            Rot = [cos(Deg) 0 sin(Deg) 0; 0 1 0 0; -sin(Deg) 0 cos(Deg) 0; 0 0 0 1];
        case 'z'
            Rot = [cos(Deg) -sin(Deg) 0 0; sin(Deg) cos(Deg) 0 0; 0 0 1 0; 0 0 0 1];
    end
end
