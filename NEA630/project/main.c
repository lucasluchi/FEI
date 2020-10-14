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


// Sinais da ignção, imobilizador e de bateria ok
#define IGN_SIG		P0_bit.no0
#define IMOB_SIG	P0_bit.no1
#define BAT_SIG		P0_bit.no2

// O sinal das portas é invertido a verificação do pino também deve ser invertida
#define DOOR1_SIG	P14_bit.no0
#define DOOR2_SIG	P14_bit.no1
#define DOOR3_SIG	P14_bit.no2
#define DOOR4_SIG	P14_bit.no3

// Sensores TPMS para vericar se a pressão dos pneus está ok
#define TPMS1_SIG	P14_bit.no4
#define TPMS2_SIG	P14_bit.no5
#define TPMS3_SIG	P14_bit.no6
#define TPMS4_SIG	P14_bit.no7

// Atuadores para acionar o motor e avisar se a pressão dos pneus está baixa
#define TPMS_LED	P7_bit.no6
#define ENGINE		P7_bit.no7


void HardwareInit (void)
{
	// configura os sinais de ign, imobilizador e bateria como entrada
	PM0_bit.no0 = 1;
	PM0_bit.no1 = 1;
	PM0_bit.no2 = 1;
		
	// configura o sinal das portas como entrada
	PM14_bit.no0 = 1;
	PM14_bit.no1 = 1;
	PM14_bit.no2 = 1;
	PM14_bit.no3 = 1;
	
	// configura o sinal do TPMS como entrada
	PM14_bit.no4 = 1;
	PM14_bit.no5 = 1;
	PM14_bit.no6 = 1;
	PM14_bit.no7 = 1;
	
	// configura o atuador do motor e LED do TPMS como saída
	PM7_bit.no6 = 0;
	PM7_bit.no7 = 0;
	
	// desliga os atuadores
	P7_bit.no6 = 0;
	P7_bit.no7 = 0;
}

void main (void)
{
	int doors_closed = 0;
	
	HardwareInit();
	
	while(1)
	{
		// verifica se todos os pneus estão com a pressão ok
		if (TPMS1_SIG == 0 || TPMS2_SIG == 0 || TPMS3_SIG == 0 || TPMS4_SIG == 0)
		{
			TPMS_LED = 1;	// acende o led indicando calibração baixa 
		}
		else
		{
			TPMS_LED = 0;	// apaga o led
		}
		
		// verifica se o sinal das 4 portas estão como fechadas
		if (DOOR1_SIG == 0 && DOOR2_SIG == 0 && DOOR3_SIG == 0 && DOOR4_SIG == 0)
		{
			doors_closed = 1;
		}
		else
		{
			doors_closed = 0;
		}
		
		// verifica o estado do TPMS, ign, imobilizador, sensor da bateria 
		// e se as 4 portas estão fechadas
		if (TPMS_LED == 0 && IGN_SIG == 1 && IMOB_SIG == 1 && BAT_SIG == 1 && doors_closed == 1)
		{
			ENGINE = 1;
		}
		else
		{
			ENGINE = 0;
		}
	}
}