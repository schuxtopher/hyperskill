spin = input()
charge = input()


if spin == "1/2":
    if charge == "-1/3":
        output = "Strange Quark"

    elif charge == "2/3":
        output = "Charm Quark"

    elif charge == "-1":
        output = "Electron Lepton"

    elif charge == "0":
        output = "Muon Lepton"

    else:
        output = "invalid charge"

elif spin == "1":
    if charge == "0":
        output = "Photon Boson"

    else:
        output = "invalid charge"

elif spin == "0":
    if charge == "0":
        output = "Higgs Boson"

    else:
        output = "invalid charge"

else:
    output = "invalid spin"

print(output)
