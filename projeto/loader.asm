            @  0
            JP F00

            @  F00
            ; carrega o endereco inicial do programa
            GD 0
            ; INICIAL_MSB e INICIAL_LSB vao ficar 0xxx, indicando 
            ; jump para endereco inicial do programa
            MM INICIAL_MSB
            ; soma 90 para POS_MEM_MSB e POS_MEM_LSB ficarem 9xxx,
            ; indicando MM da posicao inicial do bloco
            +  OP_SOMA
            MM POS_MEM_MSB

            GD 0
            MM INICIAL_LSB
            MM POS_MEM_LSB

            ; carrega tamanho do bloco
            GD 0
            MM SIZE

            ; le um byte da fita
LER_BYTE    GD 0
            JP POS_MEM_MSB
            ; soma um no endereco da memoria
RETURN_MM   LD POS_MEM_LSB
            +  UM
            ; checa se deu overflow
            JZ SOMA_UM_MSB
RETURN_OF   MM POS_MEM_LSB
            ; subtrai um do size
            LD SIZE
            -  UM
            MM SIZE
            ; checa se chegou em zero, se chegou recomeca bloco
            JZ START_BLOCK
            ; se nao chegou, le proximo byte da fita
            JP LER_BYTE

            ; carrega a posicao inicial do bloco
START_BLOCK GD 0
            ; essa soma transforma o endereco em uma operacao MM.
            ; se for end of file, GD responde com 70, logo a soma
            ; com 90 dá 00 por causa do overflow
            +  OP_SOMA
            ; se for end of file da jump pro inicio do programa
            JZ START_PROG 
            MM POS_MEM_MSB

            GD 0
            MM POS_MEM_LSB

            ; carrega tamanho do bloco
            GD 0
            MM SIZE

            JP LER_BYTE


SOMA_UM_MSB LD POS_MEM_MSB
            +  UM
            MM POS_MEM_MSB
            JP RETURN_OF

            ; zera o AC
START_PROG  LV 0
INICIAL_MSB K  0
INICIAL_LSB K  0

POS_MEM_MSB K  0
POS_MEM_LSB K  0
JP          RETURN_MM

SIZE        K  0

OP_SOMA     K  90
UM          K  1
