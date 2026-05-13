# Fake News Detection via an Adaptive Feature Matching Optimization Framework

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
The rampant proliferation of fake news across online platforms has become a significant cause for concern, necessitating the creation of robust detection techniques. Within the confines of this investigation, we present an optimization methodology built upon salient attributes tailored for the identification of fake news, spanning both unimodal and multimodal data sources. By harnessing the capabilities inherent in a diverse array of modalities, ranging from textual to visual elements, we are able to comprehensively apprehend the multifaceted nature of falsified news stories. Primarily, our methodology introduces an unprecedented array of features, encompassing word-level, sentence-level, and contextual features. This infusion bestows upon it a robust capacity to adeptly accommodate a wide spectrum of textual content. Subsequently, we integrate a feature-centric optimization technique grounded in the principles of simulated annealing. This approach enables us to ascertain the most optimal fusion of features, thereby mitigating potential conflicts and interferences arising from the coexistence of textual and visual components. Empirical insights garnered from exhaustive dataset experimentation decisively underscore the efficacy of our proposed methodology. Our approach outperforms standalone modalities as well as traditional single-classifier models, as evidenced by its superior detection capabilities. This research underscores the indispensable role played by the integration of multimodal data sources and the meticulous optimization of feature amalgamations. These factors collectively contribute to the creation of a resilient framework tailored for the identification of fake news within the intricate landscape of our contemporary, data-rich environment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors in this paper focus on the fake news detection and propose an Adaptive Feature Matching Optimization framework (AFMO) for both unimodal and multi-modal scenarios. AFMO first extracts the feature representations from diverse modals with distinct neural networks, then eliminates training instances with unnatural features by using an outlier detection approach, and designs a feature-centric optimization technique based on the principles of simulated annealing to obtain the most optimal fusion of multi-modal features followed by a MLP classifier. The experimental results demonstrate the effectiveness of the proposed AFMO framework.

### Strengths
-	The paper focuses on a practical and challenging issue, multi-modal fake news detection.
-	This paper is well-written and quite easy to follow.
-	The experimental results and ablation study show the effectiveness of the proposed framework.

### Weaknesses
-	What are the strengths of feature selection compared with the co-attention technique? The authors of this paper attempt to apply the feature selection based on the simulated annealing principle to obtain the most optimal fusion of multi-modal features. The current widely-used feature fusion technique is the co-attention. Thus, what are the strengths of feature selection compared with the co-attention technique? A more detailed discussion about this is expected. Otherwise, in the simulated annealing procedure of AFMO, “the accuracy rate emerges as the pivotal objective function governing the simulated annealing algorithm”, is it fair for other baselines?
-	Traditionally, the convergence speed of the simulated annealing algorithm is slow and it will cost more time. Thus, the time complexity analysis and real running time of AFMO are expected to be compared with baselines.
-	In the outlier detection procedure of AFMO, a preset threshold is required. How to set the threshold in the experiments, and how does the threshold affect the performance? 
-	Though CARMN leveraging the attention to fuse the multi-modal features is used as a baseline, the experimental results of another fake news detection method based on the co-attention MCAN are also expected.
-	Why does Table 5 miss the results of MKN? MKN serves as one of the baselines on the Weibo dataset in Table 4, but misses on the Gossipcop Dataset in Table 5. The performance of MKN on the Gossipcop Dataset is also expected.

### Questions
Please refer to the weakness for details.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a comprehensive optimization methodology specifically designed for fake news detection, capable of handling both unimodal and multimodal data sources. The framework is structured in four sequential steps: feature extraction, outlier removal, feature fusion, and classification. The paper validates its approach by conducting experiments on three diverse datasets: PolitiFact, Weibo, and Gossipcop. The empirical results show that the proposed framework consistently outperforms existing baselines in key metrics such as accuracy, precision, recall, and F1 score. Overall, the paper makes a robust contribution to the area of fake news detection by introducing a multi-faceted, effective methodology.

### Strengths
1. The paper leverages a variety of text features, including word-level, sentence-level, and contextual features, which help to understand the text content.
2. The paper employs a simulated annealing algorithm to optimize the feature fusion process, which is a novel and effective technique for this task.
3. The paper conducts extensive experiments on three datasets with different languages and domains, and demonstrates the superiority of the proposed framework over existing methods.

### Weaknesses
1. The paper does not provide enough details about the outlier removal step, such as how to choose the threshold for Mahalanobis distance and the number of neighbors for KNN. The lack of clarity on these parameters makes it difficult to reproduce the results and assess the robustness of the method. Specifically, the paper should detail the sensitivity of the model's performance to different threshold values and KNN neighbor sizes. Without this, it's unclear if the chosen values are optimal or if the method is highly sensitive to these parameters.
2. The baseline compared in this paper is relatively weak. As far as I know, there are many more advanced multi-modal fake news detection works. The paper should benchmark against state-of-the-art models that incorporate more sophisticated fusion techniques and attention mechanisms. This would provide a more rigorous evaluation of the proposed method's effectiveness.
3. The paper does not provide any qualitative examples or visualizations to illustrate how the framework works and why it is effective. The absence of such examples makes it difficult to gain an intuitive understanding of the method's behavior. For instance, visualizing the feature space before and after outlier removal, or showing how the simulated annealing algorithm alters feature weights, would greatly enhance the paper's clarity.

### Questions
1. What do you mean by "aberrant instances", is it deleting part of the dataset or part of the features?
2. What are the shortcomings and advantages of your method compared with other methods for eliminating multi-modal feature interference?
3. Why are the parameters of simulated annealing chosen in this way? Is there a better option? Will the cost be too high?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author has introduced an optimization method, the core of which lies in the utilization of the simulated annealing algorithm. The objective is to filter out the most informative  features of text and image features and reduce potential interference between text and visual 
information.

### Strengths
1. The paper is generally structured clearly. 
2. Experimental results show that the proposed model has comparable or improved performance.

### Weaknesses
1. The advantages and innovativeness of the proposed method appear to be somewhat limited.
2. The placement of relevant figures in the appendix makes for slightly inconvenient reading, particularly with respect to Figure 1.
3. In the experimental section, some of the recent models proposed in 2022 and 2023 have not been compared, especially the unimodal methods.
4. The position of comparative analysis（4.4.3） seems unreasonable and should be mentioned in 4.4.1.
5. The proposed model seeks to minimize potential interference between textual and visual information, but whether the feature selection through simulated annealing algorithm actually achieves the above-mentioned purpose seems to lack a detailed mechanism explanation.
6. The example in the 4.4.2 case study seems to be able to identify correctly using some methods based on capturing the similarity or ambiguity of images and texts(e.g. Cross-modal Ambiguity Learning for Multimodal Fake News Detection). I don’t know if there is a similar model in the baseline selected by the authors. This example does not seem to explain the advantages of the simulated annealing algorithm very well.

### Questions
1. The proposed model seeks to minimize potential interference between textual and visual information, but whether the feature selection through simulated annealing algorithm actually achieves the above-mentioned purpose seems to lack a detailed mechanism explanation.
2. What are the advantages compared to using neural networks like attention mechanisms to fuse features?
3. Which dataset was the experiment in Figure 2 done on? It should be noted in the text that it would be better to perform the same ablation experiments on the other two datasets.
4. The example in the 4.4.2 case study seems to be able to identify correctly using some methods based on capturing the similarity or ambiguity of images and texts(e.g. Cross-modal Ambiguity Learning for Multimodal Fake News Detection). I don’t know if there is a similar model in the baseline selected by the authors. This example does not seem to explain the advantages of the simulated annealing algorithm very well.
5. Are abnormal data removed during the running process of the comparison algorithms in Tables 4 and 5?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by the fake news detection task, the paper investigates the use of simulated annealing to perform selection of text and image features while training a multimodal neural network. The proposed framework, Adaptive Feature Matching Optimization (AFMO), consists of extracting text and image features using well-known pretrained models (BERT and VGG), removing sample outliers, and then training a feed-forward neural network while the set of active features in the input is modified by an algorithm whose proposals are accepted or rejected through simulated annealing (SA) based on the loss. The fraction of features which are "flipped" in the proposal decreases from 1.0 to 0.0 linearly as the temperature goes from t0 to tmin. The authors evaluate AFMO performance for text-only data on PolitiFact and for image+text data on Gossipcop and one of the Weibo datasets. The results indicate that AFMO outperforms all the baselines w.r.t. Accuracy, Recall and F1-score.

### Strengths
S1. While simulated annealing for feature selection has been explored by other works, this idea doesn't seem to be too explored in the context of neural networks with noisy inputs (perhaps due to the challenge of stabilizing the optimization).

### Weaknesses
W1. The text does not provide enough details for implementing the proposed feature selection algorithm.

W2. Some methodological issues, particularly regarding the use of datasets.

W3. No ablation study to understand the impact of feature selection.

W4. Novelty seems to be limited to decreasing the number of flipped features during annealing.

W5. Text is imprecise at some points and needlessly elaborate overall.

W6. Paper does not provide a way to generalize to datasets that contain environment features (e.g., comments, likes, etc).

### Questions
Q1. Many details have been left out.
- For text features, do you take the embeddings corresponding to all positions (instead of the usual approach of taking just the first position) and, if so, why? 
- Why do you need segment embeddings if the task doesn't seem to involve multiple text segments in each observation?
- Can you describe the "array of fully connected layers" at the end of the each feature extractor and that at the end of classifier?
- Does the temperature change at the end of an iteration (minibatch) or at the end of an epoch?

Q2. Please address the following concerns:
- For KNN, you don't need to normalize the dimensions by variance?
- Which multimodal Weibo dataset did you use? Jin et al., 2017 or Zhang et al., 2021a?
- Why the statistics in Table 2 do not match those in other papers (see Shu et al. 2018)? Is it showing the reduced data? Could this also explain the discrepancies between the results in Tables 4-5 and those in Hu et al., Deep learning for fake news detection: A comprehensive survey, AI Open, 2022?
- Does AFMO reduce to a BERT classifier when there is only textual data? If so, what could explain the fact that such simple model it is outperforming all the baselines on PolitiFact by a wide margin; don't you need to include a stronger baseline (e.g., dEFEND)? Or does AFMO still includes the feature selection step?

Q3. What is the performance gain of the feature selection step? What are potential alternatives for feature selection?

Q4. Please clarify what exactly are the novel contributions of the paper.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
