#include "ior5f100le.h"
#include "ior5f100le_ext.h" 
#include "intrinsics.h" 
#include "myRL78.h" 
// Configura watchdog 
#pragma location = "OPTBYTE" 
__root __far const char opbyte0 = WDT_OFF; 
// Configura detector de baixa tens�o 
#pragma location = "OPTBYTE" 
__root __far const char opbyte1 = LVD_OFF; 
// oscilador 32MHz flash high speed 
#pragma location = "OPTBYTE" 
__root __far const char opbyte2 = FLASH_HS | CLK_32MHZ; 
// debug ativado, com apagamento em caso de falha de autentica��o
#pragma location = "OPTBYTE" 
__root __far const char opbyte3 = DEBUG_ON_ERASE; 
/* Configura security ID */ 
#pragma location = "SECUID" 
__root __far const char senha[10] = {0,0,0,0,0,0,0,0,0,0};
// INICIO PADRAO


#define LED P6_bit.no3

#pragma vector = INTP1_vect
__interrupt void trata_INTP1(void)
{
	LED = 0;  // acende led
}

#pragma vector = INTP2_vect
__interrupt void trata_INTP2(void)
{
	LED = 1;  // apaga led
}

void main (void)
{
	PM6_bit.no3 = 0;	// configura LED como sa�da
	EGN0 = BIT2 | BIT1;	// INTP1 e INTP2 na borda de descida
	PIF1 = 0;			// apaga flag da INTP1
	PIF2 = 0;			// apaga flag da INTP2
	PMK1 = 0;			// habilita INTP1
	PMK2 = 0;			// habilita INTP2
	LED = 1;			// led desligado
	__enable_interrupt();	// habilita interrup��es globais
	while(1);
}