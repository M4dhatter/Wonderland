# Madhatt3r
#
#
#
#
#
#
#
#
print("    ____ _                          _               ____                _              ")
print("   / ___| |__   __ _ _ __ __ _  ___| |_ ___ _ __   / ___|_ __ ___  __ _| |_ ___  _ __  ")
print("  | |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__| | |   | '__/ _ \/ _` | __/ _ \| '__| ")
print("  | |___| | | | (_| | | | (_| | (__| ||  __/ |    | |___| | |  __/ (_| | || (_) | |    ")
print("   \____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|     \____|_|  \___|\__,_|\__\___/|_|    ")
print("v1.0 by M4dhatt3r")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Bem vindo ao Character creator, o programa para criacao de personagens de d&d3.5")
print("basta digitar oque se pede sem letra maiuscula,cedilha ou acento")
print ("")
print("")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# racas
import os
#
from random import *
elfo = str("elfo")
anao = str("anao")
humano = str("humano")
gnomo = str("gnomo")
meio_elfo = str("meio elfo")
meio_orc= str("meio orc")
halfling= str("halfling")
#
#
#
LH_for = randint(0, 7) + randint(0, 7) + randint(0, 7)
LH_cons = randint(0, 7) + randint(0, 7) + randint(0, 7)
LH_int = randint(0, 7) + randint(0, 7) + randint(0, 7)
LH_car = randint(0, 7) + randint(0, 7) + randint(0, 7)
LH_sab = randint(0, 7) + randint(0, 7) + randint(0, 7)
LH_dest = randint(0, 7) + randint(0, 7) + randint(0, 7)

forca = LH_for
constituicao = LH_cons
inteligencia= LH_int
carisma = LH_car
sabedoria= LH_sab
destreza = LH_dest
racas = [elfo, anao, humano, gnomo, meio_elfo, meio_orc, halfling]
habilidades = [forca, destreza, constituicao, inteligencia, carisma, sabedoria]
teste = habilidades
#
hab_humano = 0
#
#
#
#
#dados raciais
mod_anao_car = carisma - 2
mod_anao_cons = constituicao + 2
hab_anao = mod_anao_car, mod_anao_cons
#
#
mod_elfo_dest = destreza +2
mod_elfo_cons = constituicao - 2
hab_elfo = mod_elfo_cons, mod_elfo_dest
#
#
mod_gnomo_cons = constituicao +2
mod_gnomo_for = forca - 2
hab_gnomo = mod_gnomo_cons, mod_gnomo_cons
#
#
hab_meioelfo = 0
mod_meioelfo = 0
#
#
mod_meioorc_for = forca + 2
mod_meioorc_int = inteligencia +2
mod_meioorc_car = carisma -2
hab_meioorc = mod_meioorc_car, mod_meioorc_for, mod_meioorc_int
#
#
mod_halfling_dest = destreza +2
mod_halfling_for = forca -2
hab_halfling = mod_halfling_dest
#
#
#
#
#
#
ajuda = "ajuda"
help = "help"
print("Escolha sua raca")
chosen_race  = input()
race = chosen_race
#
#
if race == humano:
    hab_final = habilidades
if race == anao:
    constituicao = constituicao + mod_anao_cons
    carisma = carisma + mod_anao_car
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
if race == elfo:
    destreza = destreza + mod_elfo_dest
    constituicao = constituicao + mod_elfo_cons
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
if race == gnomo:
    forca = forca + mod_gnomo_for
    constituicao = constituicao + mod_gnomo_cons
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
if race == meio_elfo:
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
if race == meio_orc:
    forca = forca + mod_meioorc_for
    inteligencia = inteligencia + mod_meioorc_int
    carisma = carisma + mod_meioorc_car
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
if race ==  halfling:
    forca = forca+ mod_halfling_for
    destreza = destreza+mod_halfling_dest
    hab_final = forca, destreza, constituicao, inteligencia, carisma, sabedoria
#
#
#
#
#
def cal_mod(x):
    if x == 1:
        for_mod = -5
    if x == 2:
        for_mod = -4
    if x == 3:
        for_mod = -4
    if x == 4:
        for_mod = -3
    if x == 5:
        for_mod = -3
    if x == 6:
        for_mod = -2
    if x == 7:
        for_mod = -2
    if x == 8:
        for_mod = -1
    if x == 9:
        for_mod = -1
    if x == 10:
        for_mod = 0
    if x == 11:
        for_mod = 0
    if x == 12:
        for_mod = 1
    if x == 13:
        for_mod = 1
    if x == 14:
        for_mod = 2
    if x == 15:
        for_mod = 2
    if x == 16:
        for_mod = 3
    if x == 17:
        for_mod = 3
    if x == 18:
        for_mod = 4
    if x == 19:
        for_mod = 4
    if x == 20:
        for_mod = 5
    if x == 21:
        for_mod = 5
    if x == 22:
        for_mod = 6
    if x == 23:
        for_mod = 6
    if x == 24:
        for_mod = 7
    if x == 25:
        for_mod = 7
    if x == 26:
        for_mod = 8
    if x == 27:
        for_mod = 8
    if x == 28:
        for_mod = 9
    if x == 29:
        for_mod = 9
    if x == 30:
        for_mod = 10
    if x == 31:
        for_mod = 10
    if x == 32:
        for_mod = 11
    if x == 33:
        for_mod = 11
    if x == 34:
        for_mod = 12
    if x == 35:
        for_mod = 12
    if x == 36:
        for_mod = 13
    if x == 37:
        for_mod = 13
    if x == 38:
        for_mod = 14
    if x == 39:
        for_mod = 14
    if x == 40:
        for_mod = 15
    if x == 41:
        for_mod = 15
    if x == 42:
        for_mod = 16
    if x == 43:
        for_mod = 16
    if x == 44:
        for_mod = 17
    if x == 45:
        for_mod = 18
    return for_mod
#
#
# forca, destreza, constituicao, inteligencia, carisma, sabedoria
#
modif_for = cal_mod(forca)
modif_des = cal_mod(destreza)
modif_cons = cal_mod(constituicao)
modif_int = cal_mod(inteligencia)
modif_car = cal_mod(carisma)
modif_sab = cal_mod(sabedoria)
#
#
#
#
#
#
#
mago = "mago"
feiticeiro = "feiticeiro"
ladino = "ladino"
bardo = "bardos"
clerigo = "clerigo"
druida = "druida"
monge = "monge"
ranger ="ranger"
guerreiro = "guerreiro"
paladino = "paladino "
barbaro = " barbaro"
print("escolha sua classe")
chosen_class = input()
CH = chosen_class
classes = [mago, feiticeiro, ladino, bardo, clerigo, druida, monge, ranger, guerreiro, paladino, barbaro]
PV4 = [mago, feiticeiro]
PV6 =[ladino, bardo]
PV8 =[clerigo, druida, monge, ranger]
PV10 =[guerreiro, paladino]
PV12 =[barbaro]
PVi = 7
if chosen_class in PV4:
    PVi = 4
if chosen_class in PV6:
    PVi = 6
if chosen_class in PV8:
    PVi = 8
if chosen_class in PV10:
    PVi = 10
if chosen_class in PV12:
    PVi = 12
PV = PVi + modif_cons
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#pericias
pto_4 = [barbaro, druida, monge, ranger]
pto_2 = [clerigo, feiticeiro, guerreiro, mago, paladino]
pto_6 = [bardo]
pto_8 = [ladino]
i = 7
if chosen_class in pto_2:
    i = 2
if chosen_class in pto_4:
    i = 4
if chosen_class in pto_6:
    i = 6
if chosen_class in pto_8:
    i = 8
#
pto_pericia = (i+modif_int)*4
#
#
#
#
#
#
#encerramento
#
#
#forca, destreza, constituicao, inteligencia, carisma, sabedoria
#
#fffdfg
#
#
os.system("clear")
print("")
print("")
print("")
print("")
print("resultados")
print("")
print("sua raca")
print(race)
print("sua classe")
print(chosen_class)
print("")
print("habildades e modificadores")
print("")
print("forca")
print(forca)
print(modif_for)
print("destreza")
print(destreza)
print(modif_des)
print("constituicao")
print(constituicao)
print(modif_cons)
print("inteligencia")
print(inteligencia)
print(modif_int)
print("carisma")
print(carisma)
print(modif_car)
print("sabedoria")
print(carisma)
print(modif_car)
print("")
print("")
print("pontos de pericia")
print(pto_pericia)
print("")
print("pontos de vida")
print(PV)
print("")
print(" teste de resistencia")
print("")
print("reflexos")
print(modif_des)
print("vontade")
print(modif_sab)
print("fortitude")
print(modif_for)
print("")
print("iniciatica")
print(modif_des)
print("")
print("")
print("")
print("fim...")
print("isto foi o basico, para mais coisas pesquise no livro do jogador")
print(" mt obrigado , em breve ira ser lancadas novas versoes com mais recursos")
print("fique ligado no github")
print("-MADHATT3R-")
exit = input("aperte para sair")