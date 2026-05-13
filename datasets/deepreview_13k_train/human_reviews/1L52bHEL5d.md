# Test-Time Adaptation for Combating Missing Modalities in Egocentric Videos

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Understanding videos that contain multiple modalities is crucial, especially in egocentric videos, where combining various sensory inputs significantly improves tasks like action recognition and moment localization. However, real-world applications often face challenges with incomplete modalities due to privacy concerns, efficiency needs, or hardware issues. Current methods, while effective, often necessitate retraining the model entirely to handle missing modalities, making them computationally intensive, particularly with large training datasets. In this study, we propose a novel approach to address this issue at test time without requiring retraining. We frame the problem as a test-time adaptation task, where the model adjusts to the available unlabeled data at test time. Our method, MiDl~(Mutual information with self-Distillation), encourages the model to be insensitive to the specific modality source present during testing by minimizing the mutual information between the prediction and the available modality. Additionally, we incorporate self-distillation to maintain the model's original performance when both modalities are available. MiDl represents the first self-supervised, online solution for handling missing modalities exclusively at test time. Through experiments with various pretrained models and datasets, MiDl demonstrates substantial performance improvement without the need for retraining.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To tackle the issue of modality missing in real-time tasks, this framework offers an online self-supervised learning method called MiDl. MiDl uses mutual information and KL divergence as loss functions to optimize the model in real time, enabling the baseline model to better handle inputs with missing modalities.

### Strengths
The paper redefines the modality missing problem as a test-time adaptation (TTA) issue, emphasizing the challenges of modality absence faced in online multimodal tasks. This is indeed an urgent problem that needs to be addressed for many online multimodal tasks.

The proposed MiDl method effectively enhances the baseline model's ability to handle missing modalities, serving as a solution for the modality missing problem in multimodal online tasks. This approach can act as a supplement when facing modality absence in such tasks. For instance, if modalities are functioning normally, this pipeline may not be used; however, when a modality is missing, the proposed solution can improve the baseline model's capability to handle the missing modalities. Additionally, normal inputs and prediction results can serve as supplementary information when modalities are insufficient.

The experiments presented in the paper are comprehensive, demonstrating that the 
method is independent of modality selection, baseline models, and model frameworks, thereby proving the robustness of the proposed solution.

### Weaknesses
1. "First, the prediction of should be invariant to the modality source . Ideally, f_{\theta} should output the same prediction under both complete and incomplete modality, hence satisfying the following equality: (i)...," The underlying assumption of the approach is controversial. The task will degenerate into a modality distillation problem if this assumption holds,. Is there a more reasonable way to phrase this? The core issue is that enforcing identical predictions across complete and incomplete modalities may oversimplify the problem. In many real-world scenarios, missing modalities inherently reduce the available information, and expecting identical outputs might be unrealistic. This could lead to the model learning to ignore the specific contributions of individual modalities, rather than effectively adapting to their absence. A more nuanced approach might involve encouraging the model to produce similar, but not necessarily identical, predictions, perhaps by focusing on maintaining consistent high-level semantic interpretations while allowing for variations in confidence or detail.
2. Implementing this method in real-world production could introduce significant computational overhead and latency. Normal models can be accelerated through techniques like compression and distillation, but this approach involves updating model weights, requiring the retention of the complete model, making it difficult to deploy directly in practice. The concern is not just about the computational cost of updating weights, but also the memory footprint of maintaining the full model for online updates. This is especially problematic in resource-constrained environments or real-time systems where latency is critical. The paper should provide a more detailed analysis of the computational complexity and memory requirements of the proposed method, and perhaps explore strategies for reducing these costs, such as updating only a subset of the model's parameters or using more efficient optimization techniques.
3. Could you include experiments demonstrating the approach's decision-making in more complex online scenarios? The experiments provided in the paper do not represent the best use case for this method; its most suitable application is in online scenarios, so experiments in these contexts would better support the results. The current experiments seem to focus on relatively static datasets and do not fully capture the dynamic nature of real-world online tasks. For instance, it would be beneficial to see how the model adapts to sudden changes in modality availability, or how it handles sequences of inputs with varying modality combinations. The paper should include experiments that simulate more realistic online scenarios, such as streaming data with intermittent modality dropouts or scenarios where the statistical distribution of the input data changes over time.

### Questions
1. If this approach faces extreme examples, such as a video showing a calm street while the audio is an explosion, will this model mislead the baseline model into the wrong direction?
2. You might consider adding extra blocks to the model, so that if updates are needed, only the added portions need to be updated. Alternatively, updating part of the model's structure could prevent the significant latency introduced by updating the entire system.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles on missing modalities in egocentric videos without the need to retrain models by formulating this challenge as a test-time adaptation task. The authors proposed MiDl which minimizes the mutual information between prediction and the modality, with the incorporation of self-distillation to maintain performance when all modalities are available. The author benchmarked several methods under such problem formulation, demonstrating a descent performance when part of the modality are missing in two egocentric video datasets.

### Strengths
Overall, the paper is interesting and easy to follow. 
- The formulation of the test-time adaptation for tackling missing modality without the need for model retraining is indeed novel and can be foreseen to be applied to various applications which contains multi-modal information.
- Although the method itself is not complex and consists of components already used for various tasks for multi-modal learning and egocentric video analysis, they are leveraged in MiDl with strong motivation which are intuitive and reasonable. The extended discussion also offers a deeper understanding over the formulation of MiDl. This method could prove to be a good starting point for subsequent discussions in the research community.
- The authors also provide a comprehensive analysis over the performance of MiDl in the formulated task, and also benchmarked previous methods such as SHOT, TENT under the same setting, which also provides a further insight into the challenges and possible methods to further tackle the task.

In general, this paper is relatively well presented with a simple yet highly motivated method for an interesting formulation of a realistic challenge.

### Weaknesses
There are a few minor concerns remaining in the paper, mainly on the clarity and possible extension in discussion of the proposed method. I would like the authors to consider the following concerns if possible:
1. On Page 4, Line 197-198, the author states that "$f_\theta$ should retain high performance in predicting data with complete modality, which is generally satisfied for $f_{\theta_0}$". Does this imply that the non-adapted pretrained model must be pretrained with all modalities available? What if the pretrained model is only trained with a single modality (e.g., only with visual information without the audio information which is rather common in video models)?
2. It is observed that there is a large drop when $1-p_{AV}=100$, where none of the data contain both modalities. What would be a possible approach to mitigate this drop in performance. It is observed that the drop for MiDl is significantly more severe than that of SHOT.
3. The current method only touches upon the case for two modalities (audio and video), is it expandable towards more modalities. Also, are there limitations for the possible types of modalities or it can be any modalities as long as they are obtained from the same set of data?
4. The experiments are performed for each dataset with a drop in the primary modality, what would be the result if the secondary modality is dropped with the same probability?
5. Lastly, the code is currently NOT available, which means that the reproducibility of the result is not verified.

### Questions
Please refer to the Weakenesses section. I highly encourage the authors to directly include the code for the verification of reproducibility.

### Soundness
3

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
3

### Summary
This paper presents a novel approach to handling missing modalities in multimodal learning using test-time adaptation. The method, MiDl, shows promising results across the EPIC kitchen and EPIC sounds datasets, and the method is motivated by the theoretical intuition of minimizing the mutual information between the predicted and available modality. The authors also provide some interesting analysis of the model through long-term adaptation, out-of-distribution warmup, and various ablation experiments. 

This review follows the sections of the paper.

### Strengths
Introduction:
1. The second and third paragraphs effectively identify the gap in the literature and provide a robust overview of the proposed solution.

Related Works:

2. Related works is concise and relevant

Missing Modality as Test Time Adaptation:

3. This section is well-written and easily comprehensible.

Experiments:

4. It is commendable that the experiments were repeated 5 times with reported standard deviations in Table 11; the results appear experimentally robust and convincing.
5. The Ego4d Warmup result on 100% missing rate in the original distribution is an interesting finding with potentially strong applications.

Analysis on MiDL:

6. The Components of MiDl section is strong, and the ablations are empirically sound.

### Weaknesses
Introduction:
1. The motivation presented in the first paragraph is weak. For instance, in Line 40, could you provide an example or application where inference must occur on a redacted modality? I can think of the application of blurring faces in images or deleting private details in medical records, but it's unclear when only one modality would be completely removed for privacy reasons while the other remains intact for the same data instance. Additionally, the relevance of using cheaper modalities to missing modalities is not apparent (line 40). It would be particularly convincing if the motivation aligned with the tested dataset. For example, if using Epic Kitchens, perhaps a scenario involving a humanoid with a malfunctioning audio sensor, or smart glasses with an obscured camera due to steam or food spillage could be considered.
2. Contribution (3) appears to be describing MiDl, which is already covered in contribution (2). I would recommend reassessing what could constitute a third distinct contribution from your work.
3.Figure 1 requires improvement. The concept of a "potential performance trajectory" needs clarification - is this your hypothesis? This graphic would be more persuasive if it depicted your actual no-adaptation baseline and your TTA method. The purpose of the black line in the middle of the graph is unclear.

Proposed Solution:
4. The notation in eq (1) lacks precision. It is not evident that f(x;m) and m are random variables. The output of f is a distribution. Are you considering this as a random variable, with the value being the indices and the probability of those values the logits? Consider introducing a random variable Y ~ f(x;m). Also, consider using capital letter notation (e.g. "M") for the random variables. Furthermore, how can you evaluate the KL if x ~ S only has the modality m, not AV? Later in this section, it becomes apparent that you only update the model on complete instances. This limitation/assumption should be made clearer in the introduction or Takeaways subsection. This method would only be applicable for testing data that includes some multimodal instances.
5. At last line of page 4, is $x_t$ a single sample? Do you mean samples $x_0 \dots x_t$?

Experiments:
6. Additional details could enhance the reproducibility of this work. Was any hyperparameter tuning conducted for MiDl? Section B.1 mentions the recommended hyperparameters for the baseline but doesn't specify how they were determined for MiDl. Moreover, what were the proportions of the train/val/test split?
7. In section 5.3 LTA: You allow the model to retrain on some of the unlabeled training data. Why not gather $S_{in}$ from the validation set? In this setting, is MiDl trained on $D \ S_{in}$? Or is $S_{in}$ still included in the labeled dataset before test time and then used without labels during test time?
8. Can this method be applied to instances where either modality is missing, e.g., P = {.3,.3,.3}? It would be great to see results for experiment with such a ratio. Currently, it may be the case that the model learns to leverage ONLY the modality that is consistently present in both the complete modality test case and the missing modality test case. In this scenario, would a given unimodal model for the always-present modality perform optimally? Table 1 could be improved by clarifying what is meant by "Unimodal" and why it is only present at the 50% missing rate. For Epic Sounds, is the unimodal the always-present modality (video)?

Analysis on MiDL:
9. Both architecture choices are transformer-based. It would have been more convincing to see a greater diversity of architectures (such as a convolution backbone). Instead of presenting different missing rates as columns in Table 3, it would have been preferable to see different architectures/methods as the columns with a fixed missing rate (perhaps 50%).
10. Given that the main motivation was to avoid retraining an existing method on a large dataset to perform missing modality adaptation, the results would have been more convincing if the authors had either used an existing model+dataset and just performed adaptation, as opposed to training from scratch an existing method. Alternatively, they could have tested with a very large dataset that was computationally expensive. The omnivore pretraining test is good. Did you train the model from scratch on your dataset or use an existing model and apply MiDl?
11. In Table 6, shouldn't 55.2 in the Dl column be bolded?
12. I thought the motivation was that retraining on the train set is computationally expensive, and TTA will prevent that? It's good that you acknowledge the computational requirements of MiDl, but then in the abstract, you shouldn't state: "Current methods, while effective, often necessitate retraining the model... making them computationally intensive." Alternatively, compare your inference computation here with the amount of computation required to retrain training data (to get sufficient performance).

### Questions
While the technical aspects and experimental results are generally strong, there are areas for improvement in the motivation, clarity of presentation, and some experimental details. 

I presented many questions and suggestions in the weaknesses suggestions. In particular, I would suggest the authors focus on the concerns about the motivation and the experiments aligning with that motivation. My comments regarding notation and small fixes are merely suggestions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors focus on an important task which is test time adaptation for egocentric video action recognition under missing modality. The authors validate existing work of TTA on this new task and propose a new method MiD1 to enhance the robustness of the learned features. The performance of the proposed method is evaluated on the EpicKitchen sound and video dataset

### Strengths
1. Missing modality issue is important for test time adaptation of ego centric action recognition. This task will contribute to the community.

2. Method section is clearly written and easy to follow.

3. Compared with the baseline, the proposed approach show good performance on this new task.

### Weaknesses
1. Lack of the comparison with other approaches specifically targeted at missing modality issue.

a. Dai, Y., Chen, H., Du, J., Wang, R., Chen, S., Wang, H., & Lee, C. H. (2024). A Study of Dropout-Induced Modality Bias on Robustness to Missing Video Frames for Audio-Visual Speech Recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 27445-27455).

b. Lee, H. C., Lin, C. Y., Hsu, P. C., & Hsu, W. H. (2019, May). Audio feature generation for missing modality problem in video action recognition. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 3956-3960). IEEE.

c. Wang, H., Chen, Y., Ma, C., Avery, J., Hull, L., & Carneiro, G. (2023). Multi-modal learning with missing modality via shared-specific feature modelling. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 15878-15887).


2. The authors are suggested to enlarge the benchmarks. I aggree that this task is an important task, however the experiments are limited in this paper which will be harmful to its soundness. The authors could enrich the benchmark using more existing TTA approaches, e.g., d,e,f, and g, and try to provide an analysis on the performance on different cluster of approaches. Missing modality works can also serve as good baselines to enrich the benchmark.

d. Chen, D., Wang, D., Darrell, T., & Ebrahimi, S. (2022). Contrastive test-time adaptation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 295-305).

e. Wang, D., Shelhamer, E., Liu, S., Olshausen, B., & Darrell, T. (2020). Tent: Fully test-time adaptation by entropy minimization. arXiv preprint arXiv:2006.10726.

f. Yuan, L., Xie, B., & Li, S. (2023). Robust test-time adaptation in dynamic scenarios. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 15922-15932).

g. Niu, S., Wu, J., Zhang, Y., Chen, Y., Zheng, S., Zhao, P., & Tan, M. (2022, June). Efficient test-time model adaptation without forgetting. In International conference on machine learning (pp. 16888-16905). PMLR.

3. No qualitative reustls. The authors are suggested to provide some qualitative results when comparing their approach with the baseline approach. Some failure case analysis will be helpful.

4. The performance of the proposed approach is only verified on EPIC Kitchen, generaliyability to other dataset can be an issue.

5. TSNE visualization on the latent space will be helpful to see how the proposed supervision help during the feature learning procedure. The authors could visualize the changes for different epoches compared with its baseline.

### Questions
1. Could the authors include comparisons with other approaches specifically addressing the missing modality issue, such as those proposed by Dai et al. (2024), Lee et al. (2019), and Wang et al. (2023)?

2. Given the importance of this task, would the authors consider expanding the benchmark by including more test-time adaptation (TTA) approaches, such as Chen et al. (2022), Wang et al. (2020), Yuan et al. (2023), and Niu et al. (2022), and analyzing performance across different clusters of approaches? Including missing modality approaches as baselines may also strengthen the benchmark.

3. Could the authors provide qualitative results comparing their approach to the baseline, along with a failure case analysis to offer insights into scenarios where the method may fall short?

4. Has the generalizability of the proposed approach been tested on datasets beyond EPIC Kitchen? If not, would the authors consider verifying the performance on additional datasets?

5. Could the authors use TSNE visualization on the latent space to illustrate how the proposed supervision affects feature learning? Specifically, visualizing changes over different epochs in comparison to the baseline might provide additional insights.

### Soundness
3

### Presentation
3

### Contribution
3
