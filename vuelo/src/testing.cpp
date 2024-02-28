#include <iostream>
#include <vector>



int x; int y; int z ;int w;
int flag_angle=0;
int flag_ver =0;
int ref[4][1] = {{x}, {y}, {z}, {w}};
int flag_hor=0;


void movimiento(){
    printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
    for(int w;w<=5;w++){
        if(flag_hor == 0 && flag_ver == 0){
            for(int a=0;a<=20;a++){
                if(flag_angle == 0){
                    for(int b=360;b>=270;b--){
                        ref[4][1] = b;
                        if(b==270){
                            flag_angle = 1;
                        }
                        printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                    }
                }
                else{
                    ref[1][1] = a;
                    if(a==20){
                        flag_ver = 1;
                    }
                    printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                }
            }
        }

        if(flag_hor == 0 && flag_ver == 1){
            for(int c=0;c<=20;c++){
                if(flag_angle == 1){
                    for(int d=270;d<=0;d--){
                        ref[4][1] = d;
                        if(d==0){
                            flag_angle = 2;
                        }
                        printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                    }
               }
               else{
                    ref[2][1] = c;
                   if(c==20){
                        flag_hor = 1;
                    }
                    printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
               }
           }
        }
        if(flag_hor == 1 && flag_ver == 1){
            for(int e=20;e<=0;e--){
               if(flag_angle == 2){
                   for(int f=0;f<=90;f++){
                        ref[4][1] = f;
                       if(f==90){
                           flag_angle = 3;
                        }
                        printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                    }
                }
                else{
                    ref[1][1] = e;
                    if(e==0){
                        flag_ver = 0;
                    }
                    printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                }
            }       
        }
        if(flag_hor == 1 && flag_ver == 0){
            for(int g=20;g<=0;g--){
                if(flag_angle == 3){
                    for(int h=90;h<=180;h++){
                        ref[4][1] = h;
                        if(h==180){
                            flag_angle = 0;
                        }
                        printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                    }
                }
                else{
                    ref[2][1] = g;
                    if(g==0){
                        flag_hor = 0;
                       for(int i = 180;i<=360;i++){
                           w = i;
                           if(w == 360){
                                w = 0;
                            }
                            printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
                       }
                    }
                }
                printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);

            }       
        }
        if(w==5){
            w=1;
        }
        ref[3][1] = w;
        printf("x=%d, y=%d, z=%d, w=%d", ref[1][1], ref[2][1], ref[3][1], ref[4][1]);
    }
}

int main(){
    movimiento();
return 0;
}