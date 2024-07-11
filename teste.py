new_name = "Fonte Carregador Jfa 200a Storm Voltímetro Digital Mono 220v"

new_name = new_name.lower()
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "40a" in new_name or "40" in new_name or "40 amperes" in new_name or "40amperes" in new_name or "36a" in new_name or "36" in new_name or "36 amperes" in new_name or "36amperes" in new_name:
        modelo_escolhido = "FONTE 40A STORM"
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "60a" in new_name or "60" in new_name or "60 amperes" in new_name or "60amperes" in new_name or "60 a" in new_name:
        modelo_escolhido = "FONTE 60A STORM"
if "bob" not in new_name and ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
    if "60a" in new_name or "60" in new_name or "60 amperes" in new_name or "60amperes" in new_name or "60 a" in new_name:
        modelo_escolhido = "FONTE 60A LITE"
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "70a" in new_name or "70" in new_name or "70 amperes" in new_name or "70amperes" in new_name or "70 a" in new_name:
        modelo_escolhido = "FONTE 70A STORM"
if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
    if "70a" in new_name or "70" in new_name or "70 amperes" in new_name or "70amperes" in new_name or "70 a" in new_name:
        modelo_escolhido = "FONTE 70A LITE"
if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "90a" in new_name or "90" in new_name or "90 amperes" in new_name or "90amperes" in new_name or "90 a" in new_name:
        modelo_escolhido = "FONTE 90 BOB"
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
        modelo_escolhido = "FONTE 120A STORM"
if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
    if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
        modelo_escolhido = "FONTE 120A LITE"
if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
    if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
        modelo_escolhido = "FONTE 120 BOB"
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
    if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
        modelo_escolhido = "FONTE 200A STORM"
if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and ("mono" in new_name or "220v" in new_name or "monovolt" in new_name):
    if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:        
        modelo_escolhido = "FONTE 200 MONO"
if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
    if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
        modelo_escolhido = "FONTE 200A LITE"
if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
    if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
        modelo_escolhido = "FONTE 200 BOB"

if "k600" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name and "k1200" not in new_name:
    modelo_escolhido = "K600"
if "k1200" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name and "k600" not in new_name:
    modelo_escolhido = "K1200"
if ("controle wr" in new_name or "wr" in new_name) and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name:
    modelo_escolhido = "CONTROLE WR"
if "acqua" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name:
    modelo_escolhido = "ACQUA"
print(modelo_escolhido)