# Simplaex File Processor

## Steps to run the code:
1. Download all the files in this repository to a folder in your local machine.  
   (let us say all the files are under **~/simplaex-master/** folder).
2. Open two terminal instances (**A** and **B**) pointing to the above mentioned folder.      
3. Run the following command in **terminal A**:
```
python simplaex_file_processor.py
```
3. Run the following command in **terminal B**:
```
java -jar producer.jar --tcp
```
4. Stop both the terminals to view the result. The result csvs' will be under the **result** folder.  
   (**~/simplaex-master/result/**). Each file has the format **timestamp.csv.**

