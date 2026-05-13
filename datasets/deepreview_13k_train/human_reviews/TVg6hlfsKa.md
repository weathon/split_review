# Towards Seamless Adaptation of Pre-trained Models for Visual Place Recognition

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
Recent studies show that vision models pre-trained in generic visual learning tasks with large-scale data can provide useful feature representations for a wide range of visual perception problems. However, few attempts have been made to exploit pre-trained foundation models in visual place recognition (VPR). Due to the inherent difference in training objectives and data between the tasks of model pre-training and VPR, how to bridge the gap and fully unleash the capability of pre-trained models for VPR is still a key issue to address. To this end, we propose a novel method to realize seamless adaptation of pre-trained models for VPR. Specifically, to obtain both global and local features that focus on salient landmarks for discriminating places, we design a hybrid adaptation method to achieve both global and local adaptation efficiently, in which only lightweight adapters are tuned without adjusting the pre-trained model. Besides, to guide effective adaptation, we propose a mutual nearest neighbor local feature loss, which ensures proper dense local features are produced for local matching and avoids time-consuming spatial verification in re-ranking. Experimental results show that our method outperforms the state-of-the-art methods with less training data and training time, and uses about only 3\% retrieval runtime of the two-stage VPR methods with RANSAC-based spatial verification. It ranks 1st on the MSLS challenge leaderboard (at the time of submission).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a method to adapt foundation models to the task of visual place recognition, arguing that the object-centric focus of the training of foundation models does not align with the background/static-object attention needed in the VPR task. Thus, they propose, instead of fine-tuning the visual transformers, to extend the transform block with two mechanisms (added MLP) that operate as adapter for the global feature computation. Another local adaptation is done for reranking, similar to geometric verification of retrieved images.

### Strengths
+ concept is straightforward: the idea behind the adaptation, and the motivation why it is needed to adapt from foundation models is clearly presented.
+ experiments on relevant datasets: results are very good, improving on existing approaches
+ the paper is easy-to-read

### Weaknesses
 _very limited or non-existing insights_
 the paper is built solely around overcoming the results of existing methods, while insights and evidence-based contributions are not provided. After reading the paper I am left with a big question: "why this method works and what do I learn that can perhaps use to design methods in different applications?". Would the adaptation work also for CNNs pre-trained on ImageNet (as they share the same object-centric bias)? 
I would expect (at ICLR) a thorough analysis of reasons why the performance are much higher, what the implications of doing adaptation are, and what are the real scientific contributions behind this work (not just that the method gets better results than sota methods).

_design choice weakly explained_
no motivations or justification of why the adapters are designed in a certain way, and what the difference w.r.t. existing approaches for adaptation of foundation models are. What is the hypothesis behind this kind of design, and what explanations can be given (with experimental evidence) about their working principle?

_data-efficiency not elaborated upon_
as data-efficiency is a key argument about using foundation models, the authors indeed mention it but do not provide substantiable experimental evidence about how it benefits their approach. 

_parameter difference not well-analyzed_
The adaptation mechanisms proposed are still requiring the fine-tuning of +50M parameters, which is much more than other methods train. Summed up with the +300M parameters of the foundation backbones, these models account for much more capacity than whatever method used previously. The authors do not provide any discussion about this point, or experiments with adaptation of other (smaller) models.

A missing reference:
Leyva-Vallina et al., Data-Efficient Large Scale Place Recognition With Graded Similarity Supervision; CVPR 2023

### Questions
- How would the adapters work with other (smaller) models?
- What are the reasons, and interpretaions (with evidences) of why the proposed adapters work?
- How the adapter parameter space influences the improve of performance, and how does it relate with 'smaller' backbones?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
1.	Visual place recognition (VPR) is a fundamental task for applications in robot localization and augmented reality. This paper aims to bridge the gap between the tasks of pre-training and VPR, thus fully unleashing the capability of pre-trained models for VPR.
2.	The authors introduce a hybrid adaptation method to get both global features for retrieving candidate places and dense local features for re-ranking. 
3.	Meanwhile, a novel local feature loss is designed to guide the production of proper local features for local matching without geometric verification in re-ranking.

### Strengths
1.	This work is novel and solid. The proposed SelaVPR is a well-designed method and achieves very fast two-stage retrieval.
2.	This paper makes two technically strong contributions: closing the gap between the pre-training and VPR tasks, and outputting proper dense local features for VPR task using DINO v2. The extensive ablation experiments and visualization results show that the proposed method well adapts the pre-trained model to the VPR task. The produced dense local features also perform well in local matching re-ranking.
3.	This method achieves better performance than the SOTA methods with less training data and training time.

### Weaknesses
1.	This work adapts the pre-trained model to the VPR task. The global and local features produced by this hybrid adaptation seem to be useful for more visual tasks. Expanding the use of this method can make the contribution of this paper more obvious.
2.	The clarity of the paper could be further improved.

### Questions
1.	Why is L2 distance used to measure global feature similarity, but dot product used to calculate local feature similarity?
2.	Is it feasible to re-rank top-k candidate images directly using coarse patch tokens from ViT? and how is the performance?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a hybrid global and local adaptation method to adapt pre-trained foundation models to two-stage visual place recognition. The global adaptation is achieved by adding parallel and serial adapters in each ViT block. The local adaptation is implemented by adding up-sampling layers after ViT backbone to produce dense local features. A novel mutual nearest neighbor local feature loss is proposed to train the local adaptation module. This architecture achieves fast two-stage place retrieval and outperforms several SOTA methods. It is ranked first on the MSLS challenge leaderboard.

### Strengths
The paper is well-organized and presents a good overview of the related work.
The approach is simple and easy to follow. 
The experimental datasets are sufficient (conducted on 6 VPR benchmark datasets) and the results are excellent (outperform previous SOTA methods by a large margin).
This method can bridge the gap between the tasks of model pre-training and VPR using only a small amount of training data and training time. The two-stage retrieval runtime on Pitts30k is less than 0.1s (about 3% of the TransVPR method). This makes contributions to use pre-trained foundation models for real-world large-scale VPR applications.

### Weaknesses
This method achieves significantly better performance than other methods on several VPR datasets, and the authors qualitatively demonstrate some challenging examples. However, the motivation of the proposed method is not demonstrated well.  In particular, the gap of the tasks of model pre-training and VPR is not very clear to me. The paper mentions that pre-trained models focus on different objects than VPR models, but it does not provide a clear explanation of why this difference necessitates the proposed hybrid global and local adaptation approach. A more detailed analysis of the feature space differences between pre-trained models and VPR models would strengthen the motivation. In addition, this paper does not show failure cases, which can inform future research in VPR. Specifically, it would be beneficial to see examples where the method fails and analyze why the proposed approach is not robust in those scenarios. This would provide a more complete picture of the method's limitations and guide future improvements.

### Questions
1. Will re-ranking more candidate places achieve better performance or hurt the results?
2. This work finetunes the models on the MSLS dataset and further finetunes them on Pitts30k to test on Pitts30k and Tokyo24/7, which is the same as R2Former. However, the R2Former work provides the result on Pitts30k of the model that only trained on MSLS, which can prove the model's transferability to the domain gap. Can the proposed SelaVPR still outperform R2Former on Pitts30k using only MSLS for training?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors propose a global-local adaptation method to seamlessly adapt the pre-trained DINOv2 model to produce both global and local features for the visual place recognition task. The proposed feature representation can focus on discriminative landmarks and eliminate dynamic interference. The output local features are used in local matching for re-ranking to further boost performance. This method outperforms other state-of-the-art methods on multiple datasets with high computational efficiency.

### Strengths
1.	This paper is very well written and clearly presented.
2.	Recapitulation of related work is good.
3.	The authors design a hybrid adaptation method to seamlessly adapt pre-trained foundation model to the VPR task. The method is novel and interesting, and the authors did not over-complicate it.
4.	The experimental results are really good.

### Weaknesses
1.	Pitts250k is also a common VPR dataset. The proposed approach has shown excellent results on multiple benchmark datasets. Providing the results on the Pitts250k dataset might make the experiment more complete.
2.	Re-ranking top-100 candidates seems a common setting for two-stage VPR methods. However some works also show the performance with different numbers of re-ranking candidates [1], which can help other researchers choose the optimal number of candidates when using this method. I think it is also necessary to show the performance of different numbers of candidates.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
