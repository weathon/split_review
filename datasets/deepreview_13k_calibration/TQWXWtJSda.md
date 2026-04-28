# Unlocking the Potential of Knowledge Distillation: The Role of Teacher Calibration

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Knowledge distillation (KD) is one of the successful deep learning compression methods for edge devices, transferring the knowledge from a large model, known as the *teacher*, to a smaller model, referred to as the *student*. KD has demonstrated remarkable performance since its first introduction. However, recent research in KD reveals that using a higher-performance teacher network does not guarantee better performance of the student network. This naturally leads to a question about the criterion for choosing an appropriate teacher. In this paper, we reveal that there is a strong correlation between the calibration error of the teacher and the accuracy of the student. Therefore, we claim that the calibration error of the teacher model can be a selection criterion for knowledge distillation. Furthermore, we demonstrate that the performance of KD can be improved by simply applying a temperature-based calibration method that reduces the teacher's calibration error. Our algorithm can be easily applied to other methods, and when applied on top of the current state-of-the-art (SOTA) model, it achieves a new SOTA performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Knowledge Distillation (KD) is a successful method for compressing deep learning models. However, recent research shows that a high-performance teacher doesn't guarantee a better student. This paper introduces a criterion for choosing an appropriate teacher: the teacher's calibration error, which correlates strongly with student accuracy. The paper also presents a temperature-based calibration method that reduces the teacher's error, leading to improved KD performance. This method can enhance other techniques and achieves a new state-of-the-art performance level when applied alongside current models.

### Strengths
- Practical Applicability: The introduced temperature-based calibration method offers a practical and effective solution for improving knowledge distillation performance.

- Clarity and Conciseness: The paper effectively conveys its key findings and contributions in a clear and concise manner, making it accessible to a wide audience.

- Comprehensive Experimental Validation: The paper backs its claims with thorough experimental evaluations conducted across multiple benchmarks and domains. 

- Well-Structured Presentation: The paper is well-structured, with a clear introduction, detailed methodology, and comprehensive experimental results.

### Weaknesses
All in all, despite the simple idea and somewhat lack of novelty, the proposed method is technically sound and effective. It would be great if the authors of the paper can offer some sort of theoretical insights if possible. 

One additional experiment that is worth conducting is: intuitively, in addition to ECE, the accuracy of the teacher model would also impact the quality of knowledge distillation. Does this mean that we should favor a teacher model with better ECE and accuracy? Are there any inherent tradeoffs between accuracy and ECE among different choices of teacher models? Is it always possible to get the ECE of different models to the same level by adjusting the temperature parameter? Personally I feel that it is worthwhile conducting additional experiments using the same student model, but different teacher models of different depth to demonstrate the effect of accuracy and ECE have on the quality of knowledge distillation. This would further strengthen the empirical contribution of the paper in my opinion.  

Lastly, similar experiments were conducted previously to study the behavior between temperature and the effectiveness of knowledge distillation [1]. It would be great if a discussion is done in the related works section on the similarity and differences of this work.

### Questions
It would be great if the authors of the paper can help address the question raised in the "weakness" section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the knowledge distillation problem and reveals that there is a strong correlation between the calibration error of the teacher and the accuracy of the student. To reduce the teacher's calibration error, a temperature-based calibration is proposed.Extensive experiments demonstrate the effectiveness of the proposed method. With the help of MLLD, the proposed method achieves a new SOTA performance.

### Strengths
1. This paper is motivated well. The correlation between the calibration error of the teacher and the accuracy of the student is evaluated well (cf. Fig 1). 
2. The experimental results are strong. This work establishes new SOTAs in this field.
3. This paper is written and organized well.

### Weaknesses
1. The proposed method is too simple. The temperature scaling has been proposed in the traditional KD. The technique contribution is small.
2. Althogh this work achieves SOTA performance, it is based on previous SOTA method MLLD. All experiments are conducted on the image classification task. Object detection or other tasks are not considered.

### Questions
None

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Contemporary studies in knowledge distillation have revealed that the better teacher models could not promised the better performance of the student models. 
Motivated by this result, this paper aims to define the how to select the better teacher models. 
To this end, the authors propose a simple yet effective calibration error for the metric. 
This paper empirically demonstrates the student models well-learn the knowledge of the teacher models by applying the simple temperature scaling to the teacher models.

### Strengths
1. This paper reveals the calibration error is better than an accuracy for the metric on the knowledge distillation. 
In addition, it is convincing using the adaptive calibration error (ACE) rather than the expected calibration error.
2. This paper not only covers the most of the related studies but also is easy to follow.

### Weaknesses
It is necessary to assess whether the proposed method works well even if various calibration studies are applied. And also they should be covered in the related works.

### Questions
1. In the introduction, the authors described that two things are important in the KD process. The first is to choose an effective distillation method, and the second is to choose the best one of teachers for students. But in real-world applications, under the deployment conditions, isn't it more typical to choose a student model that can learn the best teacher model?
2. Wouldn't it be possible to reverse when T=2 and T=4?  If so, the claim is somewhat lacking in persuasion. The reason for the question is that the trend at T=4 and T=5 has reversed and also the variance of the results in Figure 2 (a) is somewhat large.
3. In Table 2, ResNet56 selected as the student model is a larger-sized model than a few teacher models (e.g., vgg19). Is this the right KD experiment?
4. After the proposed KD process, is there no need for one more calibration of the student model? I know this paper focuses on increasing the accuracy of the student model, but since it has already been learned from a calibrated teacher model, I think it is also another contribution of this paper if there is no need to conduct the calibration process for student model. Simply put, I would like to know the ECE and ACE of the student model that applied the calibration of the student model in Table 7 after applying the proposed method.


For the rebuttal, if the weakness are well addressed this reviewer is willing to raise the review score.

After discussing the authors, my concerns are solved so that I have raised my score from 5 to 6.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
