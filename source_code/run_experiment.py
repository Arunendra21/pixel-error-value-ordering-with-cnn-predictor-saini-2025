import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import build_pee_paper as B, pee_papers_content as PC
c=PC.CONTENT[17]
B._run(os.path.join(os.path.dirname(__file__),"..","figures"),
       os.path.join(os.path.dirname(__file__),"..","outputs"),[1,2,3],c["demo_key"])
print("experiment done paper 17")
