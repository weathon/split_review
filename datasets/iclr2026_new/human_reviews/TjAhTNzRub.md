## Human Reviewer 1

### Summary
This paper presents MoRE (Mixture of Remapping Experts), a novel framework for irreversible feature-level unlearning. This work mitigates existing limitations in ESC, namely, (i) the remaining set accuracy degradation, (ii) the cohesion of forget features after unlearning, and (iii) the memory inefficiency. To overcome such shortcomings, the authors propose to (i) project class prototypes into an orthogonal space, where the projected prototypes form an orthogonal basis. This allows MoRE to erase forget prototypes, without affecting the remaining ones, and to remap them to other prototypes (remaining). This disrupts separability between a specific remaining class and the forget class. By extending remapping via multiple experts, MoRE can disperse forget features to different remaining prototypes, effectively breaking the cohesiveness of such features. Experiments on established datasets and architectures demonstrate the superiority of this approach against existing baselines.

### Strengths
1. Overall, the paper is clear, well-written, and the figures help in understanding various details of the method.
2. The proposed pipeline is shown to be cheap to run both from a theoretical and empirical point of view.
3. MoRE greatly reduces the recovery of forget features after unlearning.
4. The idea is novel, interesting, and sound.
5. The pseudocode is very clear and helps in understanding the whole approach.

### Weaknesses
**Major Weaknesses**
1. The core contribution of this paper is rendering forget set features unusable for classification, and to do so, MoRE adds intermediate projections between the feature extraction and the linear classifier. This assumes black-box access to the model since, if the model is distributed, an attacker could easily recover the forgotten information by removing the added projections. To me is a great limitation and should be properly discussed in the paper. Furthermore, it is not yet clear whether unlearning only part of the model is sufficient to comply with current regulations.
2. MoRE unlearns by remapping unlearning categories to random remaining classes. It is unclear to me whether this can be applied to random unlearning. If not, the proposed method is only applicable to a subset of machine unlearning problems, which is also less relevant in my opinion. Furthermore, I fail to see how this method can be applied to, let's say, LLMs, where a class cannot be directly attributed to a logit in the output distribution.
3. Some steps in the method's formulation are unclear or not properly addressed.
   1. Lines 222-223 assume that given the prototypes matrix $P\in\mathbb{R}^{d\times k}$ and its pseudoinverse $D =V\Sigma^{-1}U^\top$, $DP=I_k$. Although this is true only if $P$ is of full rank, which is likely since $d\gg k$. Yet, I feel this should be properly discussed.
   2. Equation 4, uses $P^+$ instead of $D$ in one case. It is not wrong, but it seems like $D$ and $P^+$ are two different terms.
   3. Also in equation 4, if $DP=I$ (left inverse), shouldn't $I - PP^+=0$ (right inverse)? In that case, the complement-space projection term has no utility.

**Minor Weaknesses**
1. Figure 2 is low resolution. I suggest exporting it to PDF.
2. Line 116-117, Thudi et al. is cited twice (use \citet{})
3. Lines 214-215, the paper should clearly mention that the expected behaviours are specifically intended for class-unlearning.
4. The part on multiple experts (Section 3.3) could be more formal, in my opinion. To fully understand what is happening, I had to scroll until the appendix and check the Pseudocode.
5. Related to W2, Line 320 mentions experiments on instance-wise unlearning. Yet, I was not able to find them.

### Questions
1. Can MoRE be applied to random unlearning? If yes, how?
2. Could the authors elaborate on Weakness 3.3 (W3.3)?

**Motivation for my score** \
I feel the limitation of class unlearning is particularly concerning for the broad applicability of this method. Furthermore, the model is not actually unlearned, strictly speaking; rather, the extracted features (rich in information to be forgotten) get remapped in such a way that prevents the reuse of forgotten knowledge, forcing this method on black-box models only. Therefore, I decided to score this paper as marginally below the acceptance threshold. I am willing to change my evaluation based on the authors' rebuttal.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes MoRE (Mixture of Remapping Experts), a feature-space unlearning method designed to address three major challenges in the unlearning literature: efficiency, scalability, and irreversibility. The method constructs class prototypes and applies a prototype-orthogonal projection step to decorrelate forget and remain prototypes. It then performs remapping by scattering forget features across multiple remain prototypes through a mixture-of-experts mechanism to disrupt the coherent structure of forgotten representations. MoRE achieves strong empirical results on benchmark datasets and against multiple baselines, and offers appealing simplicity, requiring no retraining of the base model.

### Strengths
- Clear motivation and problem framing. The paper is well-motivated around three challenges in unlearning—efficiency, scalability, and irreversibility—and situates MoRE clearly within that context.

- Elegant and lightweight formulation. MoRE’s prototype-based approach provides a simple, closed-form feature-space solution that avoids full retraining and can be applied post hoc to pretrained models.

- Strong scalability, efficiency, and negligible overhead. The method scales linearly with respect to the number of samples (N), feature dimensionality (d), and number of concepts or classes (k)—O(Nd) for prototype collection and O(kd) for storage—resulting in negligible computational and memory overhead. This efficiency allows MoRE to be extended to larger models and datasets without major architectural or computational modifications.

- Strong empirical performance. The paper presents comprehensive quantitative results across multiple datasets, baselines, and model architectures, showing consistent gains in both forget success and retain utility.

- Thorough ablation studies. The ablations are detailed and informative, isolating the impact of key components such as prototype orthogonalization, remapping, and routing, and providing clear insights into their contribution to performance.

### Weaknesses
I enjoyed reading this paper and found the proposed formulation interesting and thought-provoking. I do, however, have a few points I would like to discuss with the authors:

- **Conceptual framing of knowledge deletion (KD)**. I found the paper’s framing of KD somewhat confusing. KD is described as an alternative designed to address the limitations of using retrain-from-scratch as the gold standard for unlearning. However, this seems more like a shift in objective than a solution to a known limitation. In KD, the goal is not to replicate the distribution of a retrained (oracle) model but rather to “minimize the usefulness of forget knowledge while maximizing that of remain knowledge.” This effectively corresponds to removing selected concepts while maintaining or improving utility on the rest. From that perspective, KD appears conceptually closer to model editing—which modifies or removes specific knowledge—than to classical privacy-oriented unlearning, which focuses on reproducing the retrained model’s behavior under a privacy–utility tradeoff.

- **On traditional unlearning and privacy metrics**. The claim that prior unlearning methods focus solely on privacy metrics while ignoring utility is not entirely accurate. Traditional unlearning methods already aim to balance privacy and utility by approximating the retrained model, so the key distinction from KD lies in their objectives rather than in any inherent limitations.

- **On the evaluation metrics**. Related to the previous point, I found the discussion around evaluation metrics somewhat unclear. The paper states that “By introducing utility metrics alongside privacy measures, KD no longer treats the retrain-from-scratch model as the sole point of reference, thereby enabling a more robust and practical evaluation.” However, I did not observe any new metrics being formally introduced. Traditional unlearning works already evaluate both privacy and utility—typically through accuracy on different subsets of data and membership inference attacks (MIA). The harmonic mean appears to be a concise way to summarize these results, and the KR score corresponds to accuracy after linear probing, which has also been used in prior work to assess robustness. It would be helpful if the authors could further clarify what is meant by “introducing utility metrics” and how this differs from existing evaluation practices in unlearning.

- **On the underlying assumptions and scope of applicability**. While the proposed method appears effective within its intended setting, it seems to rely on the assumption that the model functions as a closed system. My understanding is that prior to the integration of the MoRE component, the underlying feature extractor remains unchanged, meaning that any access to internal representations or earlier layers could potentially expose the forgotten information. Is this understanding correct? If so, the method would seem best suited for scenarios where third parties cannot directly access or fine-tune internal layers. It would be helpful if the authors could clarify whether this closed-box assumption is inherent to the formulation, and how the approach might behave in more open or fine-tunable settings.


- **On scalability and applicability to larger models.** The notion of knowledge deletion seems particularly relevant for large language models (LLMs), where removing specific concepts or behaviors would be highly valuable. The paper mentions that MoRE scales linearly with respect to the number of samples (N), feature dimensionality (d), and number of classes (k), which addresses computational efficiency. However, it is less clear whether this claim also extends to numerical stability and conceptual validity. As the number of classes or concepts grows, prototype orthogonalization and pseudo-inverse computations may become ill-conditioned, and the assumption that each class can be represented by a single prototype may no longer hold. It would be helpful if the authors could clarify whether the scalability claim covers these aspects or primarily refers to runtime efficiency.

- **On baseline selection**. The set of baselines compared in the paper seems somewhat limited given how active the unlearning area has become. Many new methods are introduced each year. It would be helpful to include comparisons against existing feature-based unlearning methods, as these share a closer methodological foundation with the proposed approach.

I think this is an interesting approach with practical potential, and I would be willing to revise my rating upward to an 8 if the above concerns are adequately addressed.

### Questions
I would appreciate it if the authors could clarify the following points:

- **On instance-based unlearning**: Why do you think this method can be applied in instance-based unlearning scenarios? It is not entirely clear to me whether this framework is well-suited for instance-level forgetting. The method is formulated around class/concept prototypes, which makes it naturally more compatible with class-level unlearning than with removing individual samples. Looking at Table 3, it appears that relatively little unlearning has occurred in the instance-based setup using the proposed approach. To better understand the extent of forgetting, it would be helpful if you could include the results for the original (pre-unlearning) model at the top of this table, so that the relative change in forget and retain performance can be compared directly.

- **On utility improvement**: Why do you think utility improves using this method? In particular, for CIFAR-100, the performance on D_rt
​seems to have significantly increased compared to the oracle.

- **On scalability to larger datasets**: I do not see the ImageNet results referenced in Figure 4. Does the improvement in memory and time efficiency remain significant for larger datasets?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes a method that projects forget and remain prototypes into orthogonal subspaces. By enforcing orthogonality, removing the forget prototype should not affect the remain prototype, thereby better preserving remain knowledge. In addition, the method introduces a Mixture of Remapping Experts to remap forget prototype into remain prototypes.

### Strengths
This work identifies a key limitation of existing methods that removing the forget prototype can affect the remain prototype. To address this issue, the authors propose a prototype-orthogonal projection that enforces orthogonality between the forget and remain prototypes, effectively minimizing influence on the remain information. The proposed approach sounds reasonable. 


The paper is well written and easy to follow.

### Weaknesses
1) Although the Prototype-Orthogonal projection enforces orthogonality, it implicitly assumes that the forget and remain prototypes are not highly entangled. As illustrated in Figure 2, when the entanglement is strong, the PO subspace may fail to capture the principal features of the data. In such cases, as shown in Equation (4), the introduced complement-space projection retains components of the forget prototypes. This suggests that strongly entangled forget prototypes cannot be fully unlearned, thereby limiting the effectiveness of the proposed method.

2) Experiments focus on concept-wise unlearning. The paper does not evaluate instance-wise unlearning (random forgetting), subclass unlearning, or unlearning in VLMs and generative models. This narrows the claim and leaves open whether the method robustly handles entangled features.

3) The results in Table 6 indicate that the proposed method becomes less effective in higher feature entanglement. Specifically, the stronger entanglement is in mid-layer representations, compared to the final layer. The results weaken the generality and robustness of the approach.

4) Some related works are missing and lack discussion (e.g., [1]).

[1] Deep unlearning: Fast and efficient gradient-free class forgetting.

### Questions
1) How does performance degrade as entanglement between forget and remain prototypes increases? Can you quantify this relationship (e.g., with a cosine similarity or CKA) and provide ablation studies?

2) In highly entangled cases, does the complement-space projection risk reintroducing forget information? How is leakage prevented or measured?

3) Please report results on instance-wise forgetting and subclass unlearning to support broader applicability.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes MoRE, a training-free unlearning layer that operates in a prototype-orthogonal (PO) feature space and then erases & remaps “forget” class prototypes into one or more “remain” class prototypes to destroy separability and impede recovery. The method aims to (i) preserve remain utility, (ii) achieve irreversible feature-level unlearning, and (iii) be efficient in time and memory compared to ESC method. Experiments on CIFAR-10/100, and Tiny-ImageNet evaluate performance using some conventional metrics and a feature-space Knowledge Retention (KR) probe, with ablations and efficiency comparisons.

### Strengths
1. Authors present Compelling intuition & visuals. t-SNE shows forget clusters remain separable after ESC but are absorbed or scattered under remapping and MoRE.

2. The work is well-motivated by observing the shortcoming of prior methods (e.g., separability and memory usage)

3. How authors try to address each of the problems in prior methods is clearly explained.

### Weaknesses
1. One of the core contributions as claimed by the authors is the effectiveness of using multiple experts to spread the forgotten concepts across the embedding space. Still the ablation study on the number of experts, do not support this contribution, as increasing the number of experts does not improve the results for CIFAR-100 and Tiny-Imagenet (Figure 6). Even for CIFAR-10 the results remain the same for the most part. This also can be seen from the results in Table 11.

2. When applying your method to random data forgetting, if you compute the average embedding for the forget samples in a class, it almost overlaps the average embedding for the remaining samples in that class. How do you use your method to remember the forget samples by mapping the average embedding, while maintaining the accuracy of the model on the remaining samples with the same average embedding?!

3. From the explanation it seems that each class has a single prototype vector. In that case how can the autocorrelation of a prototype vector be less than one in Figure 3? The cosine similarity of a vector with itself should be 1! This also raises questions about the discussion in section 3.1.

4. The paper seems very confusing with the use of undefined notations throughout their method section. What is S_f in line 247? The paper would benefit a lot by adding a notation section.

5. This is also the case with many undefined abbreviations (D_r, D_rt, HM, HM_t) in section 4.1.

6. The names and notations do not match across the main body, tables, and captions: $D_{rt}$ is used in the caption and D_rt in the table and text. The paper seems unpolished. 

7. A clear definition of the problem that is being solved is missing. It seems that the paper focuses on only class unlearning, but they present some results on random data forgetting in the experiments; yet, the extension of the method to unlearning a subset of the class is not clear and justified! 

8. The setting of experiments for random data forgetting is not clear at all! What percentage of data are you forgetting in the results of table 3? Are they randomly chosen across different classes? This is also the same for the classes. What is the number of classes you try to unlearn? In most class unlearning works, the main initial focus is to show that one class can be unlearned effectively and then do experiments on multiple classes. In this work authors treat classes almost as individual samples by performing bulk forgetting on multiple classes simultaneously.

9. The computation time for some of the methods seems a bit counterintuitive. For example the underlying approach for BS is similar to RL but instead of random labels it finds the labels from adversarial attacks. So the fact that the time reported for BS is much smaller than RL in figure 4 is a bit counter intuitive.

10. The SVM-based MIA that is used for evaluations is very weak compared to the SOTA MIA methods in the literature. I encourage the authors to utilize SOTA MIA for their evaluations rather than relying on basic approaches. [1] introduced is one of the SOTA MIAs that is an adaptation of  [3], but more practical with a few shadow models. There are also MIAs designed specifically to evaluate unlearning methods [2,3].

11. There are more recent works on machine unlearning for classification models that have not been used as base-lines in the experiments. Please see [4,5,6,7,8].


[1] Zarifzadeh, S., Liu, P., & Shokri, R. (2024, July). Low-cost high-power membership inference attacks. In Proceedings of the 41st International Conference on Machine Learning (pp. 58244-58282).

[2] Hayes, J., Shumailov, I., Triantafillou, E., Khalifa, A., & Papernot, N. (2025, April). Inexact unlearning needs more careful evaluations to avoid a false sense of privacy. In 2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML) (pp. 497-519). IEEE.

[3] Cadet, X. F., Borovykh, A., Malekzadeh, M., Ahmadi-Abhari, S., & Haddadi, H. (2025, June). Deep Unlearn: Benchmarking Machine Unlearning for Image Classification. In 2025 IEEE 10th European Symposium on Security and Privacy (EuroS&P) (pp. 939-962). IEEE.

[4] Zhang, B., Dong, Y., Wang, T., & Li, J. Towards Certified Unlearning for Deep Neural Networks. In Forty-first International Conference on Machine Learning.

[5] Cha, S., Cho, S., Hwang, D., Lee, H., Moon, T., & Lee, M. (2024, March). Learning to unlearn: Instance-wise unlearning for pre-trained classifiers. In Proceedings of the AAAI conference on artificial intelligence (Vol. 38, No. 10, pp. 11186-11194).

[6] Bonato, J., Cotogni, M., & Sabetta, L. (2024, September). Is retain set all you need in machine unlearning? restoring performance of unlearned models with out-of-distribution images. In European Conference on Computer Vision (pp. 1-19). Cham: Springer Nature Switzerland.

[7] Kodge, S., Saha, G., & Roy, K. (2024). Deep unlearning: Fast and efficient gradient-free class forgetting. Transactions on Machine Learning Research.

[8] Ebrahimpour-Boroojeny, A., Sundaram, H., & Chandrasekaran, V. Not All Wrong is Bad: Using Adversarial Examples for Unlearning. In Forty-second International Conference on Machine Learning. 



### Minor comments:


- In line 126 authors point out that KD is a necessary extension for MU evaluation, but they do not provide any definition or clarification for KD. At least refer to the appendix section containing the details.

- Duplicate sentence in line 717/718.

### Questions
1. In the random data forgetting setting, consider a class where some of its samples are supposed to be unlearned. Do you find one prototype for the samples that are supposed to be forgotten and one prototype for the remaining ones? How much do these prototypes differ from each other? If these points are chosen uniformly at random the average embedding of the two sets almost overlap with each other. How would it be possible to remap the forget set while retaining the model's accuracy on the remaining set?

2. What is the authors’ justification for using the mean activation vectors? Figure 1, shows the motivating example that the latent features lead to separable clusters for different classes. In that figure it seems the remapping is applied to each sample (each point in the figure) to assign it to various parts of the embedding space. However, from the Algorithm 1, that does not seem to be what the method does on individual samples, but instead it only remaps the average embedding of all the samples in one class to another part of the embedding space, which is expected to transfer all the constituting samples to that region as well, leading to a cohesive structure again. Could the authors discuss this further?


3. Why does random routing often outperform conditional? Can you diagnose expert collapse? If your conditional routing doesn’t do better than random there is no need to present it as a contribution.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
4

### Confidence
4