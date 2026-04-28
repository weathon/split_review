# GeoCon: Compositional Generalization Through Geometric Constraints on Representation Structure

- Decision: Reject
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
Compositional generalization, referring to the capacity to generalize novel combinations of fundamental and essential concepts, is thought to be the mechanism underlying a human’s remarkable ability of rapid generalization to new knowledge and tasks. Recent research on brain neural activation space has found that the geometric structure of neural representations is highly related to human compositional generalization capability.
In this paper, we extend the above observations from neuroscience to deep neural networks to validate the potential relationship between the geometric structure of representations and compositional generalization capability. In particular, we first construct a new compositional generalization benchmark from the existent datasets, which aims to discriminate multiple concepts simultaneously through a powerful representation. Meanwhile, for the aforementioned geometric constraint, the parallelism score is formally defined for deep neural networks.
Subsequently, we decompose the deep neural network into two parts: the featurizer and the classifier, to investigate the relationship between compositional generalization capability and parallelism score separately. Our proposed method, Geometric Constraint (GeoCon), involves distance variance minimization on the classifier and parallelism score maximization on the featurizer.
Experiments on synthetic and real-world datasets demonstrate significant improvement of our approach, verifying the effectiveness of our neuroscience-inspired GeoCon approach towards human-like superior generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides a mathematical formulation of parallelism score (PS) from neuroscience, and how it contributes to out-of-combination compositional generalization (CG) in deep neural networks consisting of a featurizer and classifier for classification tasks. Initial experiments on synthetic datasets reveal a strong positive correlation between PS and CG ability, but also high variance with low CG ability even for high PS. The authors propose minimum distance variance (DV) regularization to reduce such failure cases which encourages similar distance of all samples from the decision boundary. The authors also evaluate multiple pretrained models on real world datasets like PACS, NICO, and Office-Home consisting of class and domain labels, and found that the compositional generalization and parallelism score for each class is strongly correlated. However, there is a negative correlation between compositional generalization for class and domain. Self-supervised DINO and multimodal CLIP models demonstrate good compositional generalization capability for class and domain. The authors finally propose the geometric constraint (GeoCon) method maximizing PS for the featurizer and minimizing DV for the classifier to further improve CG ability across both class and domain.

### Strengths
1. The paper is well-written and easy to follow.

2. A formal description of the parallelism score from neuroscience is provided.

3. The authors propose GeoCon method which consists of two regularization techniques, one for distance variance minimization and the other for parallelism score maximization to improve the compositional generalization ability of deep neural networks.

4. The authors demonstrate the effectiveness of their method on multiple real world datasets, and the importance of both regularization techniques through ablation studies.

### Weaknesses
1. The GeoCon method seems to require a similar number of classes for each concept. 

2. The experiments are limited to datasets with only two concepts.

3. It is not clear how the method would scale to more realistic tasks, like visual question answering.

### Questions
1. How does the GeoCon method generalize when there are more than two concepts?

2. Can the authors share more details about the linear probing and finetuning baselines?

3. In Figure 8, shouldn’t the values of the parallelism score and distance variance for the models be similar at epoch=0, which is just after initialization?

4. Is the method only limited to classification problems or more generally applicable to other domains like compositional visual reasoning (e.g. COLA [1] benchmark)?

5. How many samples are required to compute the parallelism score?

[1] - Ray, A., Radenovic, F., Dubey, A., Plummer, B., Krishna, R. and Saenko, K., 2024. Cola: A benchmark for compositional text-to-image retrieval. Advances in Neural Information Processing Systems, 36.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this submission, the authors proposed a neuroscience-inspired method to tackle the problem of generalization of deep neural networks. Specifically, the authors borrow the idea of abstract representation in Ito NeurIPS 2022 to improve the compositional generalization in deep neural networks by applying geometric constraints to the representation structure, including maximizing the parallelism score of representations in the featurizer and minimizing the distance variance between sample points and decision boundary in the classifier. Results are reported on several benchmark dataset, which shows the effectiveness of the proposed method compared with linear probeing and variants of fine-tuning methods.

### Strengths
The idea of introducing the concept from neuroscience to the generalization problem of deep neural networks is interesting.

### Weaknesses
 - The idea is coming from Ito, NeurIPS 2022, which is also based on compositional generalization for neural networks. To me, the main idea is quite similar, except that the authors introduce more regularization terms (also introduced in the Ito paper) in the loss function, which is quite incremental. Can you please elaborate more on how the proposed method advances Ito, NeurIPS 2022, in case I miss something? Moreover, is it possible also to use Ito 2022 as a baseline, where the generalization capability of neural networks has been discussed (see Ito Sec 3.5)?

- While the method's evaluation focuses on class and style, and draws motivation from neuroscience, it's unclear how it advances the state-of-the-art compared to existing statistical approaches to invariant feature learning that achieve similar results. 

- While the proposed method is neuroscience-based, the results discussion is only limited to accuracy on domain generalization, which is not satisfactory. How does it benefit other generalization tasks, such as zero-shot? explainable AI?

-  I'd also like to suggest the authors consider the dataset in Ito, NeurIPS 2022, which can better help the reader to have a deeper understanding of the deep relationship between generalization and neural science (which is the main claim of the submission).

### Questions
please see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Discusses parallelism score (PS), from neuroscience, as a proxy measure of compositional generalization (CG) in artificial NNs. 

Shows that their measure of PS correlates with CG across multiple datasets and models. 

Shows that minimizing an approximation to PS, as well as an additional loss term that aims to keep points a constant distance from the classifier's decision boundary, improves CG.

### Strengths
Compositional generalization is an interesting problem.

Parallelism score seems to make sense theoretically and is generally well-explained. It is nice that it can be optimized directly, as opposed to most measures of disentanglement.

Very convincing experimental results, both in the correlation of PS and CG, and in the improvement in CG from the additional loss terms.

### Weaknesses
When introducing PS score, it's not clear to me how exactly it relates to the neuroscience measure of Bernardi et al. (2020). Presumably the latter was not able to calculate cosine similarity of different activation vectors.

Could you give more details about the datasets? what types of objects are they classifying? what are some examples of values for ‘domain’ and ‘class’?

If I understand correctly, the experiments in Section 3.2 form a test set of points that have a novel combination of class and domain, and then ‘CG class’ is the fraction of these points for which the class is predicted correctly, and the same for ‘CG domain’. In that case, I wonder how getting both correct correlates with PS score, especially in light of the fact that CG class and CG domain are negatively correlated. This is included in Tables 1 and 2, but I’d recommend saying something about it in discussing Figure 6 too. Short of putting this in as another row, ‘CG both’, in the plots of Figure 6, it would still be helpful just to mention this alternative in the text.

Section 3.2, point (iv) is confusing to me. There are only two concepts here, class and domain, what would it mean to have CG across multiple concepts?

line 364: “we can also employ an exponential smoothing method”--does that mean you do employ it?

The approximation to PS seems to require a certain amount of diversity in the batch, what batch size do you use?

The way you measure CG is very similar to Xu et al. (2022) and Mahon et al. (2024).

Line 050: “there is currently no evidence that explicitly decoupling input compositional factors substantially improves the learning efficiency or generalization capacity”--this is too strong a statement in my view. On whether there is a connection between disentanglement and CG, there are papers on both sides: those you cite claim there is not, while Higgins et al. (2016) and Esmaeli et al (2019) both claim that their methods for disentanglement show evidence of facilitating CG, and Mahon et al. (2024) claims to find a correlation between disentanglement and CG across various models and datasets. If you are to take a side on that issue, you could measure disentanglement on the embeddings you take from the frozen models in Section 3.2, and see if it correlates with CG and maybe also PS. That would be an interesting addition to your work.

**Refs**

Higgins et al. (2016) "beta-vae: Learning basic visual concepts with a constrained variational framework."

Esmaeli et al. (2019) "Structured Disentangled Representations"

Mahon et al. (2024) "Correcting Flaws in Common Disentanglement Metrics"

**Minor points**

103: “Featurizer" --> "The featurizer”

134: "the linear function" --> “a linear function”

if g and D are on the LHS of Eq (8), shouldn’t they also be on the LHS of (7) and (6)? i.e. $PS(a)$, should be $PS(a;g,D)$, or you could just remove g and D from (8) taking them to be implicit everywhere

What are $L_a$ and $L_B$ in Eq (10)? (stated earlier that they’re CE, but helpful to repeat especially before the them.)

Does 'accuracy' in Thm. 1 refer to train set accuracy?

### Questions
Could you please reply to the points I mentioned in 'weaknesses' above? (most are more questions that weaknesses) Thanks.

### Soundness
4

### Presentation
3

### Contribution
3
