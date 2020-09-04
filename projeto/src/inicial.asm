; PROGRAMA
         @  0
         ; CONFIGURA MONITOR
         LD CONFIG
         OS CFG_FILE

         ; CHAMA MONITOR PARA CARREGAR O OVERLAY
         LD CALLOV
         OS OV3
         HM 0

; DADOS
CONFIG   K  01
CALLOV   K  02
CFG_FILE K  63 ; c
         K  6F ; o
         K  6E ; n
         K  66 ; f
         K  69 ; i
         K  67 ; g
         K  2E ; .
         K  74 ; t
         K  78 ; x
         K  74 ; t
         K  00
OV1      K  01
OV2      K  02
OV3      K  03
OV4      K  04
OV5      K  05
OV6      K  06

