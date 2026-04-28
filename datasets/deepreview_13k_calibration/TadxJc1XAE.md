# TeacherActivityNet: A Novel Dataset for Monitoring Faculty Activities in Office Settings

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3

## Abstract
In this paper, we introduce a novel dataset for monitoring the activities of faculty members in academic office environments. Advances in computer vision have enabled the automation of workplace monitoring, particularly in educational institutions, where tracking faculty activities presents significant challenges and ethical considerations. Traditional methods of manual supervision are labor-intensive and prone to human error, underscoring the potential of automated video analysis as a more efficient solution. While substantial progress has been made in Human Activity Recognition (HAR) across various domains, research specifically focused on monitoring faculty activities in office settings is limited. Most existing studies concentrate on classroom and student monitoring, revealing a critical gap in faculty surveillance.
This paper seeks to address that gap by introducing TeacherActivityNet, a novel video dataset designed to recognize teachers' activities in academic offices, encompassing nine distinct action classes. We tweak the YOLOv8n architecture to propose our model, Teacher Activity Net (YOLOTAN), which is then fine-tuned using our dataset, achieving an average precision of 74.9\%, significantly outperforming benchmark models. A comparative analysis of our dataset and methods against existing solutions highlights the potential of TeacherActivityNet to improve automated faculty monitoring systems. The dataset, trained models, and accompanying code are available at https://tinyurl.com/4ub94phh

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces a video dataset to monitor faculty activities in an academic office setting. It captures nine action classes e.g., Arriving, Counselling, Idle, Working, using a cell phone camera, recorded from 19 participants in office spaces. To recognize these activities, the authors propose YOLOTAN - a modified YOLOv8n model architecture with added residual connections to improve performance in activity recognition.

### Strengths
The paper proposes to explore activity recognition in a novel office-like setting.

### Weaknesses
Ethical and privacy concerns have not been addressed - The paper does not address the underlying ethical and privacy implications of faculty monitoring. Camera surveillance and automatic activity recognition in office settings raises significant concerns particularly in an academic environment. Even if we assume that the dataset was collected with permission, this should be explicitly mentioned in the manuscript. 

Little or incremental technical contribution: 
- Slight modification to YOLO architecture by adding residual connections. No ablation study to explain why this would work for activity recognition.
- Lack of temporal modeling for video based activities.
- Lack of significant gains over comparative models.
- Limited and non-diverse dataset.

### Questions
1. What is the accuracy of state of the art video activity recognition models on the proposed dataset.
2. How well does the proposed YOLOTAN method generalize to other video-based datasets on the problem of activity recognition.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The author mentioned that the existing research had predominantly focused on classrooms and student activities, with a little intention to faulty monitoring or office settings. This effectively sets up a motivation for conducting their research. The paper’s contributions are clearly stated for a creation of a video dataset specifically capturing office activities across 9 action classes and a development of YOLOTAN model.

### Strengths
The paper introduces TeacherActivityNet, a new dataset focused on monitoring teacher activities in academic environments. It centered on educational settings which is unique and could open opportunities for specialized applications in performance analysis in office and classroom observation. The proposed YOLOTAN model showcases an effective approach to improving accuracy and speed in the YOLOv8 framework. Tables 3 through 5 present an organized summary of results to easily interpret the performance of various models in different action classes.

### Weaknesses
The paper lacks useful information or statistics about camera settings used for recording the videos for the dataset. In the data collection section, the author should describe a detailed of camera setting such as type of camera, field of view, frame rate, resolution, where the camera is set up, the distance between the actors and the camera. Please illustrate the camera setting in the experimental environment. This detail can help readers understand the conditions under which the data was collected and may influence the model performance.

The paper currently does not provide information regarding the age of the actors or the gender distribution (number of females and males) involved in the dataset. Including demographic details such as age and gender is required for understanding the context of the monitored activities.

The current work does not specify whether the actors are asked to perform actions freely or under controlled instructions. For a dataset creation task, it would be good to include whether the actions were performed spontaneously, or guided specific instructions could impact the interpretation of the dataset and subsequence model training and evaluation.

### Questions
Please include a more thorough comparison with similar datasets, such as those used for activity recognition in educational or surveillance contexts, to emphasize proposed dataset’s uniqueness or improvement over existing resources. 

If possible, please describe more details on the annotation process. It would be beneficial to know if the annotations were verified by multiple annotators or checked for consistency since the annotation quality is important for supervised learning, and inconsistencies could impact model accuracy.

Although YOLOTAN is compared to other YOLO models, comparisons to non-YOLO models commonly used in action recognition, such as those based on CNN-RNN architectures or transformer-based models, would provide a better assessment of YOLOTAN’s relative strengths and weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a data set of teacher activity monitoring to solve the problem of lack of teacher monitoring data. The work of this paper has certain significance, but there are big problems, especially in the writing, so it is not accepted for the time being.

### Strengths
see summary

### Weaknesses
1. The innovation points and problems solved in the abstract are not obvious. The author should first introduce the background content, that is, the monitoring of teachers' activities, and then explain the existing problems and the innovation points proposed in this paper. In addition, it can be seen from the abstract that the main work of this paper is to propose the data set and improve YOLOv8n, the latter proposal does not solve the corresponding problems. The length of the abstract is too long, and it is suggested that the author shorten it to less than 400 words.
2. The problem to be solved in this paper is "How to solve YOLO to effectively identify teachers' activities in the office", which is not universal. Given that the title of this article is dataset, the author should verify the reliability of the dataset through multiple methods, not just improve yolo and fine-tune yolo with that dataset.
3. It is suggested that the author expand relevant work and do not only introduce HAR. At the same time, there are too many contents about HAR, and some similar contents are repeated in the introduction.
4. The content of the introduction is weak, and there is no introduction to the problems and methods solved in this paper, especially the part about how to improve yolo.
5, it is recommended that the author check the picture and table format, the table should choose three lines as far as possible, and there should be no empty lines between the table content and the table head, as shown in Table 2 and Table 3. At the same time, adjust the image format. As shown in Figure 7, the subscripts of (a), (b), (c) and (d) are not aligned with the picture, the picture content is fuzzy, and the font is too small to see clearly. It is also suggested that the author beautify the flow chart in Figure 1.
6. I hope the author can add the introduction on how to divide teacher behavior, instead of directly dividing it into 9 actions.
7. The number of data sets provided in this paper is too small, with only 20-120 samples for each action, which lacks reference value.

### Questions
1. The innovation points and problems solved in the abstract are not obvious. The author should first introduce the background content, that is, the monitoring of teachers' activities, and then explain the existing problems and the innovation points proposed in this paper. In addition, it can be seen from the abstract that the main work of this paper is to propose the data set and improve YOLOv8n, the latter proposal does not solve the corresponding problems. The length of the abstract is too long, and it is suggested that the author shorten it to less than 400 words.
2. The problem to be solved in this paper is "How to solve YOLO to effectively identify teachers' activities in the office", which is not universal. Given that the title of this article is dataset, the author should verify the reliability of the dataset through multiple methods, not just improve yolo and fine-tune yolo with that dataset.
3. It is suggested that the author expand relevant work and do not only introduce HAR. At the same time, there are too many contents about HAR, and some similar contents are repeated in the introduction.
4. The content of the introduction is weak, and there is no introduction to the problems and methods solved in this paper, especially the part about how to improve yolo.
5, it is recommended that the author check the picture and table format, the table should choose three lines as far as possible, and there should be no empty lines between the table content and the table head, as shown in Table 2 and Table 3. At the same time, adjust the image format. As shown in Figure 7, the subscripts of (a), (b), (c) and (d) are not aligned with the picture, the picture content is fuzzy, and the font is too small to see clearly. It is also suggested that the author beautify the flow chart in Figure 1.
6. I hope the author can add the introduction on how to divide teacher behavior, instead of directly dividing it into 9 actions.
7. The number of data sets provided in this paper is too small, with only 20-120 samples for each action, which lacks reference value.

### Soundness
2

### Presentation
1

### Contribution
2
