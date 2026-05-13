# Automatic Dataset Construction (ADC): Sample Collection, Data Curation, and Beyond

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
Large-scale data collection is essential for developing personalized training data, mitigating the shortage of training data, and fine-tuning specialized models. However, creating high-quality datasets quickly and accurately remains a challenge due to annotation errors, the substantial time and costs associated with human labor. To address these issues, we propose Automatic Dataset Construction (ADC), an innovative methodology that automates dataset creation with negligible cost and high efficiency. Taking the image classification task as a starting point, ADC leverages LLMs for the detailed class design and code generation to collect relevant samples via search engines, significantly reducing the need for manual annotation and speeding up the data generation process. Despite these advantages, ADC also encounters real-world challenges such as label errors (label noise) and imbalanced data distributions (label bias). We provide open-source software that incorporates existing methods for label error detection, robust learning under noisy and biased data, ensuring a higher-quality training data and more robust model training procedure. Furthermore, we design three benchmark datasets focused on label noise detection, label noise learning, and class-imbalanced learning. These datasets are vital because there are few existing datasets specifically for label noise detection, despite its importance. Finally, we evaluate the performance of existing popular methods on these datasets, thereby facilitating further research in the field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tackles the problem of automatic dataset creation. It proposes the ADC pipeline for the same which requires minimal human overhead. The proposal is to first decide the attributes (using a LLM) and then crawl data using attribute as filters (using Google and BING APIs). This is in contrast to existing approaches that label instances given a list of classes. Finally the instances are cleaned to filter noisy labeled samples. 

The paper proposes Clothing-ADC dataset with 1M+ samples. Moreover, the paper also discusses the challenges associated with dataset construction including label errors, noisy labels and class imbalance. It then presents a solution (based on existing approaches for noise detection) to tackle these challenges to clean or improve reliability of the constructed dataset.

### Strengths
1. The paper is well written and easy to follow.
2. The paper tackles an important problem of dataset creation - the proposed approach (ADC) can do it in cost effective manner. Table 7 provides a comparison against existing label noise datasets including Cifar 10 N / H and Cifar to demonstrate the effectiveness of ADC.
3. The paper presents the Clothing-ADC dataset with 1M+ samples with 12K classes. 
4. The paper also presents a subset of Clothing-ADC CLT which is suitable for class imbalance learning. Various baselines (Drops, Bal-softmax, Logit-Adjust) are also reported for this dataset. A subset of 20K samples is also proposed for label noise detection.
5. It is important to discuss the biases (tail or infrequent classes) and noise (wrongly labeled samples) introduced due to the web data - the paper does so clearly.
6. The code and hyper-parameter details are clearly specified.

### Weaknesses
1. The ADC methodology is general; however, the paper applies it only to image data (Clothing-ADC dataset). A brief discussion can be included for other domains (such as text), if it applies. 
2. The approach is specifically designed for cases when data is fetched as part of process. It may not apply to the cases where data is available in some form such as unlabelled corpus.


### Questions
1. Please discuss the applicability of the proposed methodology for other domains such as text. How will it translate - some components (cleaning) are straightforward, others not so much (web scraping or labeling)? Please clarify if it doesn't apply. 
2. It will be helpful to have a more elaborate discussion on synthetic datasets. The paper already includes benefits of ADC over TDC. ADC should be clearly contrasted against synthetic data. Can some of the issues introduced by hallucination be recitified in cleaning stage?
3. Please include statistics for class distribution - this will provide a better idea of imbalance as well.
4. The following sentence is a bit unclear "For applications where some label noise can be tolerated, existing data curation software capable of identifying and filtering out irrelevant images, such as Docta, CleanLab , and Snorkel 1, etc."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents the Automatic Dataset Construction (ADC) pipeline, which automates the dataset creation process by leveraging large language models (LLMs) for sample collection, reducing manual annotation efforts, and enhancing efficiency in dataset generation.

### Strengths
The paper is well-organized and clearly written, easy to follow.

### Weaknesses
1. The paper’s purpose feels somewhat misaligned with practical needs. If the goal is truly Automatic Dataset Construction, the intentional design of three benchmark datasets focusing on label noise detection, label noise learning, and class-imbalance learning seems contradictory. The intent behind this approach isn’t entirely clear to me.

2. The novelty is limited, as the methodology primarily relies on leveraging LLMs to construct the dataset, which feels more like engineering work than a novel research contribution.

3. Lack of clarity regarding how the ADC pipeline addresses potential copyright and ethical concerns associated with using LLMs for data collection.

### Questions
1. Could the authors clarify the rationale behind designing specific benchmark datasets for label noise and class imbalance in the context of an automatic dataset construction pipeline? How do these benchmarks align with the overall goal of automation?

2. Given that the ADC pipeline relies on LLMs for dataset construction, what measures are in place to ensure the accuracy and relevance of data collected, especially in cases where human annotation is minimized?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Automatic Dataset Construction (ADC) a new methodology to create large-scale datasets with reduced costs and improved efficiency and accuracy. This approach leverages large language models (LLMs) for class design and sample collection, then uses various existing label error detection and robust learning techniques to enhance the quality of the dataset. The authors introduced a new dataset curated using the previously described methods, Clothing-ADC. They also developed versions of the dataset to facilitate benchmarks in label noise detection, label noise learning, and class-imbalanced learning, which they also presented comprehensive results and evaluations for.

### Strengths
1. New methodology proposed that will enable efficient dataset construction across many domains, making it adaptable for broad future applications
2. Creation of Clothing-ADC dataset which supports future work on label noise and class imbalance
3. The paper acknowledges challenges that ADC encounters when it comes to ensuring data quality, and the authors present and benchmark a comprehensive set of tools that could help to address these limitations, which helps to make the approach more viable

### Weaknesses
1. Lack of novelty in data quality methods. The paper and pipeline relies heavily on existing methods to handle label noise and class imbalance, and does not introduce any new methodologies. It mainly offers a procedural contribution rather than advancing new techniques for improving label noise or class imbalance handling
2. The paper presents many algorithms to identify label noise but is lacking detailed analysis of the impact of each algorithm on the resulting dataset and downstream model performance
3. Related to the point above, the paper does not provide quality metrics to evaluate the quality of the dataset after before/after using the ADC pipeline to clean the data, this makes it hard to assess the effectiveness of the automated curation process and ADC’s ability to produce high quality data

### Questions
1. How well will the human-in-the-loop step would scale as the dataset size gets larger, or if there is high levels of noise? Have the authors considered any ranking mechanism to prioritize samples for human review, or as another automatic filtering technique?
2. The current pipeline only checks for low-quality data in the form of noisy labels and imbalanced classes, have the authors considered how ADC could also address other data issues such as outliers, duplicates, and other low quality data (for images, that could include blurry images, odd aspect ratios etc)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors proposed propose Automatic Dataset Construction (ADC), a methodology that automates dataset creation with negligible cost and high efficiency. ADCleverages LLMs for the detailed class design and code generation to collect relevant samples via search engines. The authors design three benchmark datasets focused on label noise detection, label noise learning, and class-imbalanced learning.

### Strengths
1. The proposed Automatic Dataset Construction (ADC) leverages LLMs for the detailed class design and code generation to collect relevant samples via search engines, reducing the need for manual annotation and speeding up the data generation process.

2.  The authors explore several challenges observed in real-world dataset construction, including detecting label errors, learning with noisy labels, and class-imbalanced learning.

### Weaknesses
Could the authors please address the following questions:

1. In Step 2 of Fig. 1, the explanation for "image search engine" states, "Labeling, ADC reduces human workload by flipping the data collection process, using targets to search for samples." What is the conceptual meaning of this part?

2. In Step 3 of Fig. 1, what is the insight behind using "filter" instead of "relabeling"?

### Questions
Please the Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
