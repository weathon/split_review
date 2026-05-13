# RGB-Event ISP: The Dataset and Benchmark

- Decision: Accept
- Scores: 3, 5, 6, 8, 6

## Abstract
Event-guided imaging has received significant attention due to its potential to revolutionize instant imaging systems. However, the prior methods primarily focus on enhancing RGB images in a post-processing manner, neglecting the challenges of image signal processor (ISP) dealing with event sensor and the benefits events provide for reforming the ISP process. To achieve this, we conduct the first research on event-guided ISP. First, we present a new event-RAW paired dataset, collected with a novel but still confidential sensor that records pixel-level aligned events and RAW images. This dataset includes 3373 RAW images with $2248\times 3264$ resolution and their corresponding events, spanning 24 scenes with 3 exposure modes and 3 lenses. Second, we propose a convential ISP pipeline to generate good RGB frames as reference. This convential ISP pipleline performs basic ISP operations, e.g., demosaicing, white balancing, denoising and color space transforming, with a ColorChecker as reference. Third, we classify the existing learnable ISP methods into 3 classes, and select multiple methods to train and evaluate on our new dataset. Lastly, since there is no prior work for reference, we propose a simple event-guided ISP method and test it on our dataset. We further put forward key technical challenges and future directions in RGB-Event ISP. In summary, to the best of our knowledge, this is the very first research focusing on event-guided ISP, and we hope it will inspire the community.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a event-RAW paired dataset of pixel-level aligned events and RAW images, including 3373 images across 24 scenes, for ISP process reforming. The study presents a conventional ISP pipeline that generates high-quality RGB frames for reference, performing basic ISP operations like demosaicing and white balancing. Some existing learnable ISP methods are trained and evaluated on the dataset.

### Strengths
1. The present paper introduces a event-RAW paired dataset that addresses a gap in the field of ISP and facilitates further research on event-guided ISP. 
2. The trainable ISP methods are evaluated on this event-RAW paired dataset.

### Weaknesses
This paper, as a work primarily contributing a dataset, provides insufficient information about the dataset itself and focuses heavily on performance comparisons with existing methods, but the proposed method fails to outperform the current ones across all metrics. The overall logic and structure of the paper need improvement and refinement.
1. As a dataset-centric paper, it presents too few sample images, making it difficult for readers to intuitively grasp the specific content of the dataset and the differences in the scenes, camera shots, and exposure modes mentioned.
2. The introduction to the specific content of the dataset is insufficient. It is recommended to list statistical information about the dataset regarding the mentioned types and present them in tables.
3. The ISP presented in the paper is used to handle demosaicing, white balance, denoising, and color space transformations, but its capabilities in handling these tasks are not reflected in the performance analysis results.
4. Figures 6 and 7 have identical legends and can be combined into one figure, or one could be replaced with the visualization results of indoor data samples.
5. The experimental section only presents quantitative analysis results for outdoor and indoor data separately, failing to reflect the overall performance of the dataset.
6. The presented integrated improvement method does not enhance processing performance, and the paper does not provide sufficient explanation or analysis of this issue.
7. The experimental visual results are too few, and the layout is too compact, making it difficult for readers to intuitively appreciate the value of the dataset.
8. It is recommended to analyze the performance of different types of samples within the dataset using the same method in future work, rather than focusing primarily on comparing the performance of multiple ISP methods.

### Questions
1. The ISP method presented in this paper demonstrates varying effects across different tasks. It would be beneficial to analyze whether these effects are reflected in the proposed dataset.
2. The authors should explain and analyze the reasons why the proposed method fails to surpass existing methods in performance, as well as highlight its advantages.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a novel dataset tailored for event-guided image signal processing (ISP), featuring 3,373 high-resolution RAW images paired with corresponding event data across various scenes, exposure modes, and lenses. This dataset aims to advance RGB-Event ISP research by enabling the development of methods that directly incorporate event information within the ISP pipeline. Besides, they introduce an event-guided ISP neural network as a baseline, fusing events with RAW data to optimize ISP tasks. Then, various ISP methods are evaluated on this dataset, establishing a foundation for future RGB-Event ISP advancements. Note that this work generated high-quality RGB images as ground truth by using a ColorChecker.

### Strengths
1.	Dataset: This is the first dataset with aligned (in both time and spatial space) RAW and events from a new HVS equipment, which may provide some avenues for developing new ISP algorithms.
2.	Benchmark Task: This work evaluates the proposed dataset by testing various ISP baseline methods along with an event-guided ISP approach. Some conclusions and insights can be drawn from these experiments.

### Weaknesses
1.	Scale of the dataset: From my understanding, a robust dataset should have both scale and diversity. Although the authors mention that the dataset is relatively small due to the low stability of the HVS sensor, I am not completely convinced by it, and I still believe it would be beneficial to expand the dataset further to increase its richness and variety. Additionally, the authors could include suggestions in the future work section on strategies for scaling up the dataset.
2.	Reproducibility and Usage of the dataset: Given that this is a dataset/benchmark paper, I strongly encourage the authors to release the data as soon as possible, even during the review stage. Early access is crucial for the community to begin evaluating and utilizing the dataset.
3.	Benchmark Task: This dataset is tailored for RAW-Event ISP tasks. So, I wonder if we should focus more on designing various Event-guided ISP baselines. In the current setup, most baselines do not utilize the event data, raising concerns about whether these limited event-guided baselines effectively demonstrate the dataset’s potential. I believe increasing the variety of event-driven baselines could better validate the usefulness of this dataset and highlight its unique contributions to event-guided ISP research.

### Questions
My questions are highly overlapped with the weakness as follows:
1.	Dataset Scale and Diversity: Could you provide more insights into the limitations that prevented a larger dataset collection, and provide more insights about how to scale up the data?
2.	Early Data Release: Is there a timeline or plan for public release of the dataset, especially considering its importance for community validation and use? 
3.	Event-Guided ISP Baseline Evaluation: Given that the dataset is designed for RAW-Event ISP tasks, consider developing additional baseline methods that explicitly incorporate event data to better assess the dataset's strengths. For instance, could you explore a wider variety of event-guided architectures or fusion methods to better showcase the potential of the event data in ISP?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce the first events-RAW paired dataset specifically designed for event-guided image signal processing (ISP) research. This dataset comprises 3,373 high-quality, high-resolution RAW images alongside corresponding pixel-level aligned events. Using a controllable ISP pipeline developed by the authors, high-quality RGB frames are generated. A thorough evaluation and analysis of existing learnable ISPs, as well as a straightforward event-guided ISP method, are performed on this dataset. From this analysis, the authors highlight several key points and challenges associated with event-guided ISP.

### Strengths
1. The relevant background knowledge of this paper is clearly explained.

2. The topic of RGB-event ISP is very interesting topic and meanful for future camera.

3. The writing is very well and easy to understand.

### Weaknesses
1. I greatly appreciate the effort to create a dataset for RGB-Event ISP, which opens up opportunities for event-assisted RGB ISP tasks. However, the dataset's scale is quite limited, with only 3,373 samples, which may not be sufficient to support data-driven learning methods. This raises concerns about the dataset's ability to serve as a professional, standardized, and challenging benchmark. If this is primarily a workload issue, could the authors consider generating some simulated datasets? I would appreciate an explanation regarding this.

2. The authors use images generated from a controllable ISP framework based on MATLAB as ground truth. While they provide extensive explanations for this approach, it is difficult to trust software-generated images as ground truth, especially for a professional dataset. This practice differs significantly from the ground truth methods used by existing sensor or smartphone manufacturers for their ISPs.

3. The integration of events into traditional ISP theoretically brings certain advantages, and the authors should elaborate on these benefits. Additionally, to demonstrate the advantages of event cameras, the authors should showcase scenes, particularly under high-speed motion or extreme lighting conditions, that highlight the potential benefits of using event-based approaches.

### Questions
Please see the weaknesses. I have assigned a preliminary score based on the initial manuscript and will consider adjustments depending on the authors' responses and feedback from other reviewers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the RGB-Event ISP dataset and benchmark, a novel paired dataset that combines RAW and event data from hybrid vision sensors to support research in event-guided image signal processing (ISP). The authors design a customizable ISP pipeline, allowing for benchmarking ISP methods and exploring the benefits of integrating event data in RAW-level ISP tasks. The experiments demonstrate the effectiveness of several methods in both outdoor and indoor scenes, and the dataset offers unique insights into ISP improvements through event data.

### Strengths
1. The dataset fills an existing gap by providing paired RAW and event data, which is the first of its kind specifically designed for ISP tasks.
2. The proposed ISP pipeline is flexible, covering key ISP stages like black level adjustment, demosaicing, and color correction, making it versatile for testing various ISP algorithms.
3. The experimental evaluation is thorough, comparing several state-of-the-art ISP methods and highlighting the advantages of using event data, particularly in dynamic outdoor scenes.
4. The paper also addresses its limitations and suggests potential solutions. Specifically, it provides practical insights into the challenges of integrating event data with ISP, including issues like artifacts under artificial indoor lighting.

### Weaknesses
1. The dataset size is relatively small (3373 images), which might limit the generalizability of models trained on it. Additional data, particularly with more diverse scenes and lighting conditions, could enhance the applicability of the findings. The limited size may also lead to overfitting when training complex deep learning models, thus hindering the real-world performance of these models.

2. The theoretical justification for how event data contributes to each ISP stage could be more developed. For instance, while the paper mentions the use of event data, it lacks a detailed explanation of how the high temporal resolution of event data specifically enhances tasks like white balancing, demosaicing, and noise reduction. A more rigorous analysis of the underlying mechanisms and how event data complements traditional ISP algorithms would strengthen the contribution. Specifically, the paper should discuss the mathematical formulations or signal processing techniques that leverage event data for these tasks.

3. The writing lacks clarity, making the paper difficult to understand for readers not deeply familiar with the field. Enhancing the language clarity and providing more structured explanations, particularly in the methodology section, would significantly improve the paper's readability and accessibility. The inconsistent use of terminology, such as the spelling error of 'convential' instead of 'conventional,' further contributes to this issue. Additionally, the omission of 'density' in the y-axis label of Figure 5c is a significant oversight that should be corrected.


### Questions
1. In Section 3.1, it would be helpful to elaborate on the role of event data in each ISP stage (e.g., how it improves demosaicing or color correction compared to using RAW data alone).
2. There are some spelling errors in the paper. For instance, both "convential ISP pipeline" and "conventional ISP pipeline" appear, where "convential" is incorrect; it should be "conventional ISP pipeline." Additionally, in Figure 5c, the y-axis should be labeled as "probability density," but the word "density" seems to have been omitted. 
3. My concern is that some comparative algorithms have very low PSNR scores. From the varying performance of PyNET and UNet under different hyperparameters, I believe it would also be beneficial to test CameraNet with different hyperparameters. This would allow us to select a high-performance configuration as a baseline, ensuring a fairer and more comprehensive comparison.
4. I have a question regarding the alignment between APS (Active Pixel Sensor) and EVS (Event-based Vision Sensor) data. As mentioned in the paper, there is a significant difference in their frame rates. How is the event data aligned with the RAW data given this disparity in FPS?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new event-RAW paired dataset collected with a novel but private sensor that records pixel-level aligned events and RAW images. 3373 RAW images with paired events spanning 24 scenes are captured. A convential ISP pipeline is proposed to generate RGB references and learnable ISP methods are used to train and evaluate on the dataset.

### Strengths
1. Event-guided ISP seems like a novel and interesting idea.
2. A novel sensor is designed to capture the datasets, although it's private and confidential.
3. The analysis and results looks good.

### Weaknesses
1. The proposed is rather small-scaled. There are 24 videos captured in total, with 80 to 140 frames for each video. Considering a FPS of 60, it's just 1-2 seconds. It would be better called an image dataset instead of a video dataset.
2. I assume the dataset would be open-sourced? Although the paper does not explicitly state that.
3. As the authors stated, the prototype is cumbersome with low stability and also private. This weakens the reproducibility of the work.
4. The background of the dataset and issues need further clarifications. It is not clear to me at the moment.

### Questions
Please explain what is 'event' (with examples) and why event camera is important in addition to RGB camera, maybe in the introduction/related work section. This is important for readers unfamiliar with this topic.

### Soundness
2

### Presentation
3

### Contribution
2
