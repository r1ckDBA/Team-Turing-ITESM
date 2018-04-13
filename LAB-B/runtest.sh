echo  "Begin Automated Testing."
cd /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Probelma1/
python3 -m unittest oddOrEven_unittest.py  2> /home/ubuntu/test_results/oddOrEven.log

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema2/
python3 -m unittest  Lab2-list-UNITEST.py  2>  /home/ubuntu/test_results/Lab2-list-UNITEST.log

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema3/
python3 -m unittest listAnalysis3_unitTest.py  2> /home/ubuntu/test_results/listAnalysis3_unitTest.log

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema4/
python3 -m unittest fileOverlap_unittest.py  2> /home/ubuntu/test_results/fileOverlap_unittest.log

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema5/
python3 -m unittest reverseWord5_unitTest.py  2> /home/ubuntu/test_results/reverseWord5_unitTest.log

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema6/
python3 -m unittest Lab6-cowsbulls-UNITEST.py  2> /home/ubuntu/test_results/Lab6-cowsbulls-UNITEST.log

cd /home/ubuntu/test_results
find . -name '*.log' | xargs grep -i "OK" -nr $1  | tee >(wc -l)

echo "Static Analysis Results"

echo "Evaluating oddOrEven.py"
cd /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Probelma1/
nohup pylint3 oddOrEven.py 2> /home/ubuntu/test_results/oddOrEven_static_analysis.log &

echo "Evaluating Lab2listconfusion.py"
cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema2/
nohup pylint3 Lab2listconfusion.py 2> /home/ubuntu/test_results/Lab2listconfusion_static_analysis.log &

echo "Evaluating listAnalysis3.py"
cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema3/
nohup pylint3 listAnalysis3.py 2> /home/ubuntu/test_results/listAnalysis3_static_analysis.log &

echo "Evaluating fileOverlap.py"
cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema4/
nohup pylint3 fileOverlap.py 2> /home/ubuntu/test_results/fileOverlap_static_analysis.log &

echo "Evaluating reverseWord5.py"
cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema5/
nohup pylint3 reverseWord5.py 2> /home/ubuntu/test_results/reverseWord5_static_analysis.log &

echo "Evaluating Lab6cowsbulls.py"
cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/Problema6/
nohup pylint3 Lab6cowsbulls.py 2> /home/ubuntu/test_results/Lab6cowsbulls_static_analysis.log &

echo "Generate Documentation"

cd  /var/lib/jenkins/workspace/Free\ Style\ Project/LAB-B/
doxygen oxigen_config_labc

echo "Done "
