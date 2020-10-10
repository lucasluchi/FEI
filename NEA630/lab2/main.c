#include "ior5f100le.h"
#include "ior5f100le_ext.h" 
#include "intrinsics.h" 
#include "myRL78.h" 
// Configura watchdog 
#pragma location = "OPTBYTE" 
__root __far const char opbyte0 = WDT_OFF; 
// Configura detector de baixa tensão 
#pragma location = "OPTBYTE" 
__root __far const char opbyte1 = LVD_OFF; 
// oscilador 32MHz flash high speed 
#pragma location = "OPTBYTE" 
__root __far const char opbyte2 = FLASH_HS | CLK_32MHZ; 
// debug ativado, com apagamento em caso de falha de autenticação
#pragma location = "OPTBYTE" 
__root __far const char opbyte3 = DEBUG_ON_ERASE; 
/* Configura security ID */ 
#pragma location = "SECUID" 
__root __far const char senha[10] = {0,0,0,0,0,0,0,0,0,0};
// INICIO PADRAO


void main(void)
{
PM5_bit.no2 = 1; // port P52 como entrada  Chave SW1
PM5_bit.no3 = 1; // port P53 como entrada  Chave SW2

PM7_bit.no0 = 0; // port P70 como saída LED 1 
PM7_bit.no1 = 0; // port P71 como saída LED 2
PM7_bit.no2 = 0; // port P72 como saída LED 3 


P7_bit.no0 = 1; // apaga LED 
P7_bit.no1 = 1; // apaga LED 
P7_bit.no2 = 1; // apaga LED
PU5 = BIT3; // liga pull-up interno de P53 chave SW2


while(1)
	{
		while(P5_bit.no2==0 && P5_bit.no3==1)
			{ //chave SW1 fechada  e SW2 aberta
				P7_bit.no0 = 0; 
			}
		P7_bit.no0 = 1;
		while(P5_bit.no2==1 && P5_bit.no3==0)
			{//chave SW1 aberta  e SW2 fechada
				P7_bit.no1 = 0;
			}
		P7_bit.no1 = 1;
		while(P5_bit.no2==0 && P5_bit.no3==0)
			{//chave SW1 fechada  e SW2 fechada
				P7_bit.no2 = 0;
			}
		P7_bit.no2 = 1;
	}
}