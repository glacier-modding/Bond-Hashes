import os
import json
import argparse
import string
from common import ioi_hash

parser = argparse.ArgumentParser(description="Bruteforce DLGE paths from sounddefs.json files")
parser.add_argument('-i', '--input', type=str, required=False, help="Path to folder containing sounddefs.json files.")
parser.add_argument('-o', '--output', type=str, default="bruteforced_dlge_paths.txt", help="Output file name. Defaults to bruteforced_dlge_paths.txt.")
args = parser.parse_args()

found = []

for dirpath, dirnames, filenames in os.walk(args.input):
    for filename in filenames:
        if filename.endswith('.sounddefs.json'):
            full_path = os.path.join(dirpath, filename)
            
            with open(full_path, 'r') as file:
                data = json.load(file)

                characterName = data.get('name')

                for definition in data.get('definitions'):
                    definitionStripped = definition.lstrip('0123456789 ')
                    
                    if definitionStripped.lower().startswith("vox_"):
                        dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/vox_combatant_{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                        found.append(dlgePath)
                    
                    elif definitionStripped.lower().startswith("dsguse_"):
                        for letter in string.ascii_lowercase:
                            dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/dsguse_{letter}_npcsee_{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                            found.append(dlgePath)
                    
                    elif definitionStripped.lower().startswith("sntry_"):
                        for letter in string.ascii_lowercase:
                            dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/sntry_entryno_{letter}_{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                            found.append(dlgePath)

                    elif definitionStripped.lower().startswith("inter_"):
                        dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/inter_interrupt_{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                        found.append(dlgePath)

                    elif definitionStripped.lower().startswith("cmbt_rnfrcecallcr_"):
                        dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/cmbt_rnfrcecallcr_seq_{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                        found.append(dlgePath)

                    else:
                        dlgePath = f"[assembly:/_knt/localization/knt/conversations/ai_dialog/{characterName}/{definitionStripped}_{characterName}.sweetdialog].dialogevent"
                        found.append(dlgePath)

with open(args.output, "w") as f:
    for item in found:
        f.write(f"{item}\n")
