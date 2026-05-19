### Summary

This paper proposes a new method for OOD detection, called AbeT. The main idea is to replace the scalar temperature in the energy score with a learned temperature. Experiments are conducted on classification, object detection, and semantic segmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method AbeT is simple and easy to implement.
- The proposed method AbeT is lightweight and introduces almost no additional computational cost.
- The proposed method AbeT achieves strong performance on classification, object detection, and semantic segmentation.

### Weaknesses

#### Some Related Works

[1] Extremely simple activation shaping for out-of-distribution detection.
[2] The devil is in the gradients: Assessing the robustness of deep image classifiers.
[3] A simple unified framework for detecting out-of-distribution samples and adversarial attacks.
[4] MaxLogit: A simple baseline for out-of-distribution detection.
[5] MaxLogit cannot detect out-of-distribution samples.
[6] Generalized out-of-distribution detection: A survey.
[7] React: Out-of-distribution detection with rectified activations.
[8] On the importance of gradients for detecting distributional shifts in the wild.
[9] Extremely simple activation shaping for out-of-distribution detection.
[10] Max logit probability is unreliable for out-of-distribution detection.

#### comment

 - The proposed method AbeT is not novel. The learned temperature is an extension of the existing method [1]. The energy score is an extension of the existing method [2]. The proposed method AbeT simply combines the learned temperature and the energy score.
- The proposed method AbeT is not well motivated. The authors claim that the temperature learned by [1] is learned to be high on inputs on which the classifier is uncertain (line 210). If this is true, it would be natural to claim that the temperature learned by [1] would lead to the energy score being closer to 0 on OOD inputs. The authors should provide a theoretical analysis to support their claim that the Forefront Temperature Constant counteracts the desired property.
- The proposed method AbeT is not well evaluated.
  - The authors should evaluate the performance of AbeT on the challenging OOD detection benchmarks, including near-OOD [3], SSB [4], and iSSB [5]. These benchmarks are crucial for assessing the robustness of OOD detection methods, and the lack of evaluation on these datasets limits the impact of the work.
  - The authors should evaluate the performance of AbeT on large-scale datasets, including ImageNet-1k [6]. The current evaluation is limited to smaller datasets, and it is unclear how the method would scale to more complex and realistic scenarios.
  - The authors should evaluate the performance of AbeT on the challenging OOD detection methods, including React [7], GradNorm [8], DICE [9], and ASH [10]. Comparing against these methods would provide a more comprehensive understanding of the strengths and weaknesses of AbeT.
  - The authors should evaluate the performance of AbeT on the challenging classification datasets, including CIFAR-100 and ImageNet-1k. The current evaluation is limited to CIFAR-10, which is a relatively simple dataset.
- The authors should compare the performance of AbeT with the performance of the combination of [1] and [2]. It is not clear whether the proposed method AbeT is better than the simple combination of the two existing methods.
- The authors should compare the performance of AbeT with the performance of the existing methods in a fair evaluation setting. The authors should use the same backbone architecture and the same training hyperparameters for all methods. The current evaluation setting is not fair, and it is unclear whether the performance gains are due to the proposed method or the differences in the evaluation setting.
- The authors should provide the code to reproduce the results. The lack of code makes it difficult to verify the claims made in the paper.

### Suggestions

The paper's primary weakness lies in its limited novelty and insufficient experimental validation. While the idea of combining a learned temperature with an energy score is intuitive, the paper fails to adequately demonstrate the unique contribution of this combination. The authors should provide a more rigorous theoretical justification for why the Forefront Temperature Constant counteracts the desired property of the energy score. A deeper analysis of the interaction between the learned temperature and the energy score is needed to understand the method's behavior. Furthermore, the paper should include a comparison with the simple combination of the two existing methods to demonstrate the advantage of the proposed approach. The current evaluation is not comprehensive enough to establish the effectiveness of the proposed method.

To address the evaluation concerns, the authors should conduct experiments on more challenging OOD detection benchmarks, such as near-OOD, SSB, and iSSB datasets. These benchmarks are essential for assessing the robustness of OOD detection methods. The authors should also evaluate the performance of AbeT on large-scale datasets like ImageNet-1k to demonstrate its scalability. Additionally, the paper should include comparisons with state-of-the-art OOD detection methods, such as React, GradNorm, DICE, and ASH. These comparisons are crucial for understanding the strengths and weaknesses of AbeT relative to existing approaches. The current evaluation is limited to a single dataset (CIFAR-10) and a few baselines, which is not sufficient to establish the generalizability of the proposed method. The authors should also evaluate the performance of AbeT on more challenging classification datasets, such as CIFAR-100 and ImageNet-1k.

Finally, the authors should ensure a fair evaluation setting by using the same backbone architecture and training hyperparameters for all methods. The current evaluation setting is not fair, and it is unclear whether the performance gains are due to the proposed method or the differences in the evaluation setting. The authors should also provide the code to reproduce the results. The lack of code makes it difficult to verify the claims made in the paper. The authors should also provide more details about the implementation of the proposed method, including the specific architecture used for the learned temperature and the training procedure. This would help other researchers to reproduce the results and build upon the proposed method.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
