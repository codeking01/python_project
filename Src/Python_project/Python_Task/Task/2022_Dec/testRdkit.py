# author: code_king
# time: 2022/12/25 15:21 
# file: testRdkit.py
from rdkit import Chem

testsmi = '[H][C@@]12CC[C@H](O)[C@@]1(C)CC[C@]1([H])C3=C(CC[C@@]21[H])C=C(O)C=C3'
mol = Chem.MolFromSmiles(testsmi)
Chem.MolToMolFile(mol, 'output.mol')