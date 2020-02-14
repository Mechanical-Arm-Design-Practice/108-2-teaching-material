function main()
    clf;
    fram = 200;
    for i= 1:1:fram
        Aorg = [0 0 0]'; %起始點座標中心
        AorgVecxyz = [1 0 0; 0 1 0; 0 0 1]'; %起始點各軸向量

        AtmpVxyz = [];
        for j= 1:1:3
            AtmpVxyz = [AtmpVxyz HomoRot('z',180*i/fram)*HomoRot('y',90*i/fram)*HomoRot('x',90*i/fram)*([AorgVecxyz(:,j) ;1])] %各軸同時旋轉向量(可自行更改或新增旋轉)%角度為單位
        end
        AendVecxyz = AtmpVxyz;
        
        Atmp =  HomoTra(1*i/fram,0*i/fram,0*i/fram)*[Aorg; 1];%暫存終點座標中心位移(可自行更改位移) %座標向量1為單位
        
        Aend = Atmp(1:3,:);%終點座標中心
        Ax = [Aend(1)+AendVecxyz(1,1) Aend(2)+AendVecxyz(2,1) Aend(3)+AendVecxyz(3,1)];%終點座標之x軸末端點
        Ay = [Aend(1)+AendVecxyz(1,2) Aend(2)+AendVecxyz(2,2) Aend(3)+AendVecxyz(3,2)];%終點座標之y軸末端點
        Az = [Aend(1)+AendVecxyz(1,3) Aend(2)+AendVecxyz(2,3) Aend(3)+AendVecxyz(3,3)];%終點座標之z軸末端點
    
        plot3([Aend(1) Ax(1)],[Aend(2) Ax(2)],[Aend(3) Ax(3)],'r-o'); %畫出x軸，並刷新畫面
        hold on
        plot3([Aend(1) Ay(1)],[Aend(2) Ay(2)],[Aend(3) Ay(3)],'g-o'); %畫出y軸，並刷新畫面
        hold on
        plot3([Aend(1) Az(1)],[Aend(2) Az(2)],[Aend(3) Az(3)],'b-o'); %畫出z軸，並刷新畫面
        hold off
        axis([-5 5 -5 5 -5 5]);grid on; %設定界限
        
        drawnow 
    end
%% 練習2 p.14
    Aorg = [7, 3, 2]'
    %Ans = HomoTra(4,-3,7)*HomoRot('y',90)*HomoRot('z',90)*[Aorg; 1]
    Ans = HomoRot('z',90)*[Aorg; 1];
    A = HomoRot('z',90)
%% 範例2 p.16
   B = HomoTra(0,1,1)*HomoTra(-0.6,0.4,0)*HomoTra(0.1,0.1,2)*HomoRot('x',180)*HomoRot('z',-90)

end


function Tra = HomoTra(x,y,z) % 齊次座標平移轉換矩陣
    Tra = [1 0 0 x; 0 1 0 y; 0 0 1 z; 0 0 0 1];
end

function Rot = HomoRot(xyz,Deg) % 齊次座標旋轉轉換矩陣
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
