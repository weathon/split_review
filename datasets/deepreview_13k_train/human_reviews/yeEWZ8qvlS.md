# Learning Interpretable and Influential Directions with Signal Vectors and Uncertainty Region Alignment

- Decision: Reject
- Scores: 6, 3, 5, 5, 6

## Abstract
Latent space directions have played a key role in understanding, debugging, and fixing deep learning models. Concepts are often encoded in distinct feature space directions, and evaluating impact of these directions on the model's predictions, highlights their importance in the decision-making process. Additionally, recent studies have shown that penalizing directions associated with spurious artifacts during training can force models to unlearn features irrelevant to their prediction task. Identifying these directions, therefore, provides numerous benefits, including a deeper understanding of the model's strategy, fostering trust, and enabling model correction and improvement. We introduce a novel unsupervised approach utilizing signal vectors and uncertainty region alignment to discover latent space directions that meet two key debugging criteria: significant influence on model predictions and high level of interpretability. To our knowledge, this method is the first of its kind to uncover such directions, leveraging the inherent structure of the feature space and the knowledge encoded in the deep network. We validate our approach using both synthetic and real-world benchmarks, demonstrating that the discovered directions effectively fulfill the critical debugging criteria.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces an unsupervised method for discovering interpretable and influential directions in the latent space of deep neural networks, specifically for image classifiers. The proposed approach leverages signal vectors and uncertainty region alignment to identify latent space directions that significantly influence model predictions while maintaining high interpretability. Unlike previous methods that require annotated concept datasets and predefined concepts, this method does not rely on prior knowledge and instead learns from the inherent structure of the feature space. The authors validate their approach on both synthetic data and real-world benchmarks, demonstrating that the discovered directions effectively fulfill critical debugging criteria and outperform supervised methods in certain aspects.

### Strengths
The paper presents a novel unsupervised framework for discovering latent space directions that are both interpretable and influential. This is an advancement over prior work that often requires annotated datasets or predefined concepts.

The method is theoretically grounded, extending previous models to a multi-label setting and introducing new loss functions such as the Uncertainty Region Alignment loss. The experimental results on synthetic and real-world data support the efficacy of the approach.

### Weaknesses
While the experiments are promising, the evaluation is limited to a synthetic dataset and a single real-world dataset (Places365 with ResNet18). A broader range of datasets and models would strengthen the claims and demonstrate the generalizability of the method. Specifically, the method's performance on datasets with varying complexities, such as those with fine-grained categories or different image modalities, remains unclear. Furthermore, the choice of ResNet18, a relatively shallow network, may not fully reveal the method's capabilities when applied to deeper, more complex architectures. The lack of evaluation on models trained with different optimization strategies or data augmentation techniques also limits the understanding of the method's robustness.

The paper could provide a more thorough comparison with existing methods, including additional baselines in both interpretability and influence metrics. This would help in positioning the proposed method within the existing literature more effectively. For interpretability, a comparison against methods that explicitly learn disentangled representations or concept-based models would be beneficial. For influence, the evaluation should include a broader range of techniques that aim to identify influential directions in latent spaces, not just limited to methods that focus on concept signal estimation. The current comparison lacks a comprehensive analysis of the trade-offs between interpretability and influence achieved by the proposed method versus existing approaches.

### Questions
Is the proposed method applicable to other types of data beyond images, such as text or time series data? If so, what modifications, if any, would be necessary?

How does the method scale with larger models and datasets? Are there computational bottlenecks, and if so, how can they be mitigated?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method to learn interpretable and influential directions in a trained model’s latent space, where these directions are modeled as linear “signal” classifiers. The authors propose a method called Uncertainty Region Alignment that aligns the subspaces where the model is uncertain and the subspaces where the learned “signal” classifiers are also uncertain, with the claim that this enhances the interpretability and influence of the learned directions. They present results from a small synthetic setting and from a slightly larger, more realistic setting on a single model and dataset (Resnet18, Places265), where they benchmark against IBD and find that their method produces better concept detectors.

### Strengths
* The problem of finding concepts or latent directions that are highly influential, which I take to mean causal, is an interesting and very active research area at the moment. Being able to use interpretability tools to exert influence over a model would be of high utility for future research and real-world applications.

### Weaknesses
 - As it stands, it was difficult for me to understand the contribution of this work with respect to prior literature in this field. Further discussion of how this paper relates to the wide body of recent literature on generating concept-based explanations, including follow-up works to ACE/ICE/IBD such as CRAFT [1], work on Concept Bottleneck Model literature [2, 3, 4, 5], and recent work on sparse autoencoders and dictionary learning, would help clarify the gap in existing literature that this paper is trying to fill.
- Furthermore, it seems like this paper is a close follow-up to the papers by Doumanoglou et al. (2023; 2024) cited in the paper, in that the majority of the method is the same with some minor adjustments. Can you provide further discussion of how this method and its contributions differs from the methods in those two papers?
- The writing and presentation of this paper are not very clear to me - I struggled to understand the types of explanations given by the proposed method, and how those explanations could be used to gain a  “deeper understanding of the model’s strategy, fostering trust, and enabling model correction and improvement” as stated by the authors in the abstract. Clarifying the intent of the proposed method and how the experiments validate its practical applications with respect to the stated goals from the abstract and introduction would significantly improve the paper.
- Given that this paper is an explainability/interpretability paper, I believe it could strongly benefit from providing some example explanations yielded by the paper, and a more in-depth example or case study of how the explanations can be applied to the aforementioned end goals of model correction.

### Questions
- Are the learned directions always labeled by NetDissect? I would appreciate some clarity on how NetDissect is being applied to the proposed method and its necessity in generating explanations. If so, why is the proposed method preferable to simply using NetDissect on its own?

- Please see above weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to automatically learn the set of concept vectors underlying a given model representation in an unsupervised manner. Specifically, given a model representation and an unsupervised image dataset, the method aims to extract a set of "signal" vectors that explain the representation, and are semantically meaningful. Experimental results show that (1) in synthetic settings where the ground truth signals are known, the proposed method recovers the ground truth; and (2) when applied for an image classification setting, the extract signal vectors score high on numerical interpretability metrics.

### Strengths
+ The topic of extracting a set of contributing semantic concepts underlying a representation is an important topic, that can potentially help efforts in debugging and controlling model behaviour. 

+ The proposed method is somewhat empirically successful, in that it is able to recover ground truth signals in synthetic settings; and recover signal vectors that score high on numerical interpretability metrics.

### Weaknesses
This paper is **hard to read**. At times, the issue is missing details, and at other times, it makes lots of references to text in the appendix and/or other papers. For instance, the method defines six heuristic loss functions, however it is unclear how they are combined and how the regularization parameters are set. The exact definitions and motivations for these are sometimes buried in the appendix. In addition, several terms defined in individual papers (Doumanoglou et al. (2023), Pfau et al. (2020), and Pahde et al. (2024)) are used without defining or explaining them. In particular, the contributions in these listed individual papers (S^1;S^2 interpretability metrics, RCAV, and Pattern CAV) are unexplained and used without context in the paper. I recommend that the authors rewrite these sections by clearly explaining the method, including being explicit about the exact loss functions used and the optimization problem being solved. In addition, it would help if terminology from other papers is first clearly defined before being used.

**Missing Comparison with PCA / ICA / Dictionary learning**: One of the goals of this paper is to recover signal and distractor vectors that combine additively to generate the underlying inputs. However, this is precisely the setting in which classical methods such as PCA / ICA / dictionary learning are applicable (depending on the exact underlying assumptions re: orthogonality, etc), and the missing discussion and comparison with these methods in the context of this paper is a significant omission. An experiment comparing the proposed method with such classical baselines would help build the case for the proposed approach. In addition, it would be helpful to point out what is conceptually missing in such classical approaches that necessitates the present one.

It is **unclear whether recovered signals are interpretable**, in the sense that an unambiguous assignment exists from the signal vector to a semantic concept. In the interpretability literature, including network dissection (Bau et al., 2017), it has been discussed that not all nodes are interpretable in the sense that an assignment to a semantic concept is not always possible. If the authors can present visualizations of the set of recovered signal vectors and discuss what makes them interpretable, this would help claim the interpretability benefits of this approach.  

**Minor**: The paper claims that its method overcomes a common weakness of concept-based methods, i.e., the requirement of annotated concept datasets (line 88). However, even the proposed method uses the Broyden concept dataset to annotate concept labels (line 412), and without this, it is unclear how the method recovers interpretable signals.

### Questions
- The "M" term used in the maximum margin loss does not appear in any other loss equations (except perhaps in equation 5, where it seems to be a different "M"). Can you please clarify how the margin loss "M" is calculated?

- Line 451 mentions "Significant Direction Count (SDC) and Significant Class-Direction Pairs (SCDP). SDC represents the number of learned signal vectors that significantly influence at least one of the model’s classes, while SCDP counts the total number of class-direction pairs in which the learned signal vector significantly affects the class." -> what is "significantly influenced" here?

- Conceptual clarification: Is the assumed data generation process in equation 1, identifiable? For example, if s_1 and s_2 are two signal directions, then is s_1 + s_2 also a signal direction? 

- Conceptual clarification: given a candidate direction "v", what is a simple test to determine whether it is a signal or a distractor direction?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a method to identify interpretable and influential directions in latent spaces of deep learning models. Since the latent space directions play a crucial role in understanding and correcting deep models, the goal here is to identify directions in the latent space that influence model predictions while being interpretable. Traditional approaches for finding these directions rely on supervised methods and predefined concepts. This paper introduces an unsupervised framework that combines signal vectors with uncertainty region alignment to discover interpretable latent directions.

### Strengths
1. The attempt to discover influential directions in a model's latent space without relying on labeled data is good. If it works, it will make the method more scalable compared to other techniques that require manual annotation or predefined concepts.

2. The method has been tested not just on synthetic datasets but also on real-world tasks using state-of-the-art models like ResNet18. 

3. The writing can be improved by incorporating more motivations in introducing each loss.

### Weaknesses
While I commend the authors for developing an unsupervised method to identify interpretable directions, the approach faces a key challenge. Supervised methods generally ensure that these directions align closely with actual concepts, providing a clearer sense of interpretability. But unsupervised methods can not guarantee that.

The paper lacks experiments that measure cosine similarity with "ground truth concept vectors" on real datasets, such as Places365. This raises doubts about the authenticity of the learned vectors, as evidenced by the significant performance gap between unsupervised and supervised methods in Table 4. Putting together, if the learned "concept vector" doesn’t reliably represent the true concept, the claim of interpretability becomes less compelling.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents an unsupervised method for discovering interpretable and influential latent space directions in deep-learning models using signal vectors and uncertainty region alignment. The approach is validated on synthetic and proof-of-concept real-world data, showing its effectiveness in recovering key signal directions and improving model debugging.

### Strengths
- The presented method is very well theoretically motivated and is a valuable extension to existing (supervised) discovery methods like CAV.
- The experiments have been carried out accurately and with care. However, I would classify both experiments more as proof-of-concepts than real-world experiments as the places365 dataset is very limited in complexity. However, this is totally valid in my opinion, as the focus of the paper is the theoretical contribution.
- The ablation studies on the loss components are extensive and interesting.

### Weaknesses
 **W1:** The paper is sometimes hard to follow and understand. While in the methods section, the equations help to understand what’s described in the text, the different experiments are sometimes hard to follow. Especially for a reader unfamiliar with latent space-based concept methods for interpretability the different methods and the interpretation of their results can be confusing. For example, the experiment setup in 4.1 and how it connects to section 2 could be better explained. The experiment setup in 4.2 refers to several methods from related work (e.g. Network Dissection, Broden dataset, RCAV (which was never introduced)), which readers are possibly not familiar with. 

To improve clarity, I suggest adding an overview of key concepts at the start of the experiments section, explicitly explaining how Section 4.1 connects to Section 2, and providing brief explanations for unfamiliar methods (not limited to) like Network Dissection, the Broden dataset, and RCAV when they are first introduced.

**W2:** The authors comment in Line 297 that experiments with the raw inclusion of the three loss terms do not converge, but do not further elaborate on how stable the final results are with their adaptations, i.e. if the learned directions are robust. 

Please provide quantitative measures of the robustness in the learned directions, e.g. through the standard deviation or confidence intervals over several differently seeded runs for the tables in section 4 (if applicable).

**W3:** Figures 1 and 2 are very helpful in communicating the concepts but are never referred to in the main manuscript. The paper would benefit from a general overview figure in the same style (in which these two figures would be a part), similar to a graphical abstract to communicate the different steps and concepts visually.

Please provide an overview figure on how the presented method is composed (and maybe why certain selections were made) in section 3. If it would make sense for you, also integrate Figure 2 into this overview figure.

**W4:** The paper lacks a published code repository, making it difficult for others to easily apply the method to their own models.

Please provide a link to an anonymous repository with a (simple) implementation of the method. You can use "Anonymus Github" or GitLab with an anonymous email. 

I am open to raising my score if the identified weaknesses are either adequately addressed through revisions to the manuscript or convincingly argued to be non-issues.

### Questions
See weaknesses W1 to W4.

### Soundness
4

### Presentation
2

### Contribution
3
