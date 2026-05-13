# SEEKER: Semi-Supervised Knowledge Transfer for Query-Efficient Model Extraction

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Model extraction attacks against neural networks aim at extracting models without white-box access to model internals and training datasets. Unfortunately, most existing methods demand an excessive number of queries (up to millions) to reproduce a functional substitute model, greatly limiting their real-world applicability. In this work, we propose a query-efficient model extraction attack that effectively distills knowledge from publicly available data. To this end, we we introduce a semantic alignment approach that trains the substitute model without interacting with the victim model. The proposed approach optimizes the substitute model to learn a generalizable image encoding pattern based on semantic consistency of neural networks. We further propose a query generator that enhances the information density of generated queries by aggregating public information, thereby greatly reducing the query cost required for constructing the substitute model. Extensive experiments demonstrate that our method achieves state-of-the-art performance which improves query-efficiency by as much as 50× with higher accuracy. Additionally, our attack demonstrates the capability of bypassing most types of existing defense mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a query-efficient model extraction framework including query-free self-supervised training and query-efficient query generator. The proposed SEEKER method shows superior experimental results on multiple benchmark datasets.

### Strengths
The paper is well written and easy to understand. The idea of applying self0supervised training for model extraction is interesting.

### Weaknesses
The method itself, although works great, seems a bit ad-hoc. It will be great to see some theoretical justifications behind the framework.

### Questions
See weakness.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Model extraction attacks focus on creating a substitute model whose performance resembles a victim model’s performance; this is achieved by querying the victim model with a selection of samples and observing the output behavior. Among other things, doing so allows whitebox adversarial attacks to be used to target the victim model. This particular paper proposes two major components for improving such attacks. The first is a semantic alignment, done both as offline pre-training and during querying. The second is a way of parallelizing the query generation process by encoding the information of multiple samples into a single sample. The result is a method that is much more query-efficient than prior methods, gaining high substitute model, fidelity, and attack success rate with far fewer queries, while also being strong in the large query regime as well.

### Strengths
## S1. Query efficiency
A central claim of this paper is that the proposed method reduces the number of queries needed to perform a successful attack. This is important as a large number of queries renders a method slow and computationally expensive, while also significantly raising the risk of being detected (and stopped) by the target system. Figure 5 effectively illustrates how much faster the substitute model’s metrics can improve using the proposed approach vs the baseline methods. Highlight claim is that this can be up to 50x more query efficient.

## S2. Empirical Results
The empirical results of this paper are generally strong. Again, Figure 5 provides an excellent summary, showing higher accuracy, fidelity, and ASR vs competing methods, with fewer number of queries. At the (very) high query range, the proposed approach also shines (Table 2), barely edging out DFMS-SL. Results also appear to generalize to other model architectures (Table 3).


## S3. Generally clearly written
The paper is clearly written and easy to understand. That said, the paper could still use another round of editing: there are a few typos, some potential improvements to the technical notation, and a number of other issues to fix (see Miscellaneous under Weaknesses). Overall though, this paper was easy to read.

### Weaknesses
## W1. Novelty
Semantic consistency is presented as one of the two methodological improvements proposed by the authors. The concept, however, doesn’t strike me as particularly new. Offline semantic alignment is simply self-supervised pre-training on a different dataset (very reminiscent of [b], in fact); it’s not particularly surprising that this is helpful, as that’s more or less the whole point of self-supervised learning. The similarities in Grad-CAM visualizations doesn’t necessarily have much to do with model extraction: it may be more due to having stronger features, which presumably the victim model also has, resulting in strong correlation. Online semantic consistency is more or less just knowledge distillation [d] with augmentations.

## W2. Aggregation Design
a) Why the query perturbation/residual is added to the first input sample $x_{pub,1}$ (as opposed to, say, $x_{pub,2}$) isn’t clear and seems like an arbitrary choice. It would seem like there could be a smarter way to select which of the $m$ samples to chose as the base sample. \
b) It’s also not clear to me why there is a separate encoder per query index. As far as I can tell, the relative ordering of queries within a parallel batch is not meaningful, so there doesn’t seem to be any added value behind having separate encoders, vs just having a single shared encoder or some other permutationally invariant design (e.g. a transformer).\
c) I don’t fully understand the design of the reconstruction loss. Why do we care about reconstructing the input data? We already have the input data. Rather than generating new images through an encoder and decoder, what about simpler methods like MixUp or CutMix? The formulation in Equation 3 also involves a significant number of hyperparameters $\alpha_j$ to tune, and it’s not clear why they should be meaningfully different; as in b) above, it doesn’t seem like the order of the samples have any inherent meaning, so why for example should $\alpha_2 \neq \alpha_3$?

## W3. Source of empirical improvements
The ablation study in Section 4.4 is very helpful, but it’s also somewhat concerning too. From this table, it appears that the offline semantic alignment is the bulk of the source of improvements. While doing this offline semantic alignment is reasonable, as stated in W1 above, it’s really another name for starting off with a stronger substitute model through standard self-supervised pre-training, which is already well known by the community to be generally effective for many downstream tasks. The form of self-supervised learning used by the authors is fairly standard, so it’s not clear to me if this really can be counted as the authors’ contribution.

## W4. Section 4.5
Analysis of the proposed method’s performance against defense mechanisms is welcome, but most of the actual results (particularly the paragraph on “Passive Defenses”) appear to be absent from the main paper and deferred to the Appendix. If these analyses are going to be introduced in the main paper, then at least some quantitative results should be included.

## Miscellaneous:
- pg 2: “Mosafi et al.(Mosafi et al., 2019)” <= use in-text citation
- pg 3: “with [a] generative adversarial network”
- Section 2.2: This section leaves out transfer-based blackbox attacks, which generate attacks on the attacker’s own model, which are then given to the target (victim) model. Such approaches have also been combined with query-based attacks, with very low query requirements, e.g. [a].
- pg 4: “a[n] aggregated”
- pg 4: Why not denote $x_{pub}$ as $x_p$ instead, to match $D_P$?
- pg 4: “$i$-th query dataset” <= isn’t this just a sample and label, not a dataset?
- pg 4: “that share the same weight[s]”
- pg 4: This is a standard Siamese network approach to self-supervised learning; more such methods should be cited: e.g. [b,c]
- pg 5: “we [a] propose aggregated query generator”
- Eq 5: If I’m understanding this loss correctly, I think this is for the $i+1$th iteration, not $i$th. Also, as written, this implies we only care about a new query sample not resembling the immediately previous query; this doesn’t prevent a query for example from flipping back and forth between two queries.
- pg 6: “Second, [w]e design”
- Fig 5: Caption should mention what dataset this is on. Text doesn’t mention it either.
- Table 2: What dataset is this? Text doesn’t say either.
- Table 3: What dataset is this? Text doesn’t say either.
- Table 4: What dataset is this? Text doesn’t say either.


[a] Inkawhich, Nathan, et al. "Perturbing across the feature hierarchy to improve standard and strict blackbox attack transferability." NeurIPS 2020. \
[b] Chen, Xinlei, and Kaiming He. "Exploring simple siamese representation learning." CVPR 2021.\
[c] He, Kaiming, et al. "Momentum contrast for unsupervised visual representation learning." CVPR 2020.\
[d] Hinton, Geoffrey, Oriol Vinyals, and Jeff Dean. "Distilling the knowledge in a neural network." 2015.\

### Questions
Q1. How does the similarity of the public dataset to the target model’s dataset affect results? The main results in Table 1 show significant overlap: CIFAR-10 is used as the public dataset when CIFAR-100 is the hidden dataset, and vice versa, and even Tiny-ImageNet has strong similarities compared to CIFAR 10/100.\
Q2. Is the substitute model the same architecture as the victim model? Is that a reasonable assumption to make? What if they’re different?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the vulnerability of Deep Neural Networks (DNNs) to model extraction attacks, even when the models are accessed in a black-box manner. These attacks allow adversaries to create a substitute model that mimics the original model by querying the black-box model with unlabeled inputs. The paper introduces SEEKER, a query-efficient model extraction framework that leverages semi-supervised public knowledge transfer. The framework incorporates an offline stage for pre-training the substitute model without any query costs, a semantic alignment scheme, and a multi-encoder query generator. Experimental results indicate that SEEKER significantly improves query efficiency while maintaining high accuracy and attack success rate (ASR) compared to state-of-the-art methods.

### Strengths
1. SEEKER introduces a novel approach to model extraction that combines offline pre-training with semantic alignment, reducing the need for extensive querying. The paper claims that SEEKER can reduce the query budget by over 50 times compared to existing methods while achieving comparable or better accuracy.
2. The experimental results are thorough and clearly presented.

### Weaknesses
I like the technical merit in this paper. My major concerns are around the presentation that might require significant modification of the main body. I'm willing to raise the score if the following concerns are addressed.
1. In the methodology part, there is no explicit discussion or intuition why the proposed method can improve the query efficiency, i.e., reduce the number of queries. If so, what is the query efficiency just a side effect? We need more justification that only experimental results. 
2. The paper presents a complex methodology without providing much intuition. I can get a main idea of whole methodology. But the motivation of each part is not clear. For example, in section 3.2, why a good framework should be designed this way.

### Questions
Is it possible to provide a simpler graph than Figure 1 for illustrating the main idea?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
