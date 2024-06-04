What it does:
The repo conatains two file ie OU_Results_Fetcher.py and Result_Visualizer.py .
It fetches results of batch of students or class at a single time and create a excell file containg the results and also visualizes it.
The visualization is done in three ways. first one is a bar graph of students roll no and thier respective GPAs.
The second one is overall passed and promoted students pie chart.
The third one is Bar graph of number of students failed in specified subjecs.
YOU CAN SEE THE IMAGES ATTACHED BELOW FOR BETTER UNDERSTANDING
Here is the step by step procedure with example images:
1. clone the repository in your pc or you can do it in the terminal by copying and pasting this code in you terminal

   git clone https://github.com/Ishxaq/OU-Result-Fetcher/tree/main
   
   cd OU-Result-Fetcher

   pip install -r requirements.txt

   now you can skip step 2 if you pasted this on terminal.

3.  install the necessary dependencies by running pip install -r requirements.txt  in the terminal after moving in the cloned dir of this repo.
4. change the range of roll no in the OU_Results_Fetcher.py file and the link to results
   
   ![image](https://github.com/Ishxaq/OU-Result-Fetcher/assets/171219614/9bc3a8fb-46a5-4a68-962c-60c29c0085a3)

5. This will create a excell file of the results for the desired roll nos in the same dir as this file.
6. Now to visualize this data open the Result_Visualizer.py and update the location of the excell file. Also upadte the name of your class

   ![image](https://github.com/Ishxaq/OU-Result-Fetcher/assets/171219614/3187da31-7494-4a0e-8003-285ae8818145)

7. Now run this file it will create three photos back to back.
   first is a bar graph of roll no vs GPA of the students

   ![image](https://github.com/Ishxaq/OU-Result-Fetcher/assets/171219614/76e81723-d103-4843-a46c-911eef5ff360)


   second is overall passed and promoted pie chart

    ![image](https://github.com/Ishxaq/OU-Result-Fetcher/assets/171219614/aaacb84b-dd0b-4388-8e0a-bd74c672282e)

   and third is a bar grapgh of number of students failed in particular subjects.Note you might need to update the subject names here if you are from other department or sem.

   ![image](https://github.com/Ishxaq/OU-Result-Fetcher/assets/171219614/a7c854f4-c510-4e65-bd2b-f1bc391653a2)




