# Single-Step Diffusion Model-Based Generative Model Inversion Attacks

- Decision: Reject
- Scores: 5, 5, 6, 3, 3

## Abstract
Generative model inversion attacks (MIAs) have garnered increasing attention for their ability to reconstruct synthetic samples that closely resemble private training data, exposing significant privacy risks in machine learning models. The success of generative MIAs is primarily attributed to image priors learned by generative adversarial networks (GANs) on public auxiliary data, which help constrain the optimization space during the inversion process. However, GAN-based generative MIAs still face limitations, particularly regarding the instability during model inversion optimization and the fidelity of reconstructed samples, indicating substantial room for improvement. In this paper, we address these challenges by exploring generative MIAs based on diffusion models, which offer superior generative performance compared to GANs. Specifically, we replace the GAN generator in existing generative MIAs with a single-step generator distilled from pretrained diffusion models, constraining the search space to the manifold of the generator during the inversion process. In addition, we leverage generative model inversion techniques to investigate privacy leakage issues in widely used large-scale multimodal models, particularly CLIP, highlighting the inherent privacy risks in these models. Our extensive experiments demonstrate that single-step diffusion models-based MIAs significantly outperform their GAN-based counterparts, achieving substantial improvements in traditional metrics and greatly enhancing the visual fidelity of reconstructed samples. This research uncovers vulnerabilities in CLIP models and opens new research directions in generative MIAs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DDMI (diffusion distillation model inversion attacks), a novel approach that improves upon traditional GAN-based model inversion attacks by using distilled single-step diffusion models. The method shows superior performance in reconstructing private training data from both classification and CLIP models, demonstrating better visual quality, stability, and attack success rates compared to existing methods. Beyond technical improvements, the work is significant as the first to explore privacy vulnerabilities in CLIP models, highlighting urgent needs for better privacy protection in machine learning systems.

### Strengths
1. First attempt to explore CLIP model vulnerabilities
2. Good visualization of results

### Weaknesses
1. The core idea of replacing GANs with diffusion models have limited technical depth without fundamental insights into privacy mechanisms.
2. No theoretical gurantee of privacy such as Differential privacy or other theoretical foundations.

### Questions
1. How does this method fundamentally advance our understanding of privacy vulnerabilities beyond showing that better generative models lead to better attacks?
2. Why choose SiD specifically for distillation? What are the trade-offs compared to other distillation methods?

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
This work studies techniques for improving generative Model Inversion Attacks (MIA) in white-box settings. The major contributions of this work are:

1) In the context of model inversion attacks, this paper identifies key limitations of GAN-based generative MIAs, namely unstable optimization and low-fidelity sample reconstruction (Fig. 1). To address these challenges, the authors propose a framework called DDMI (Diffusion Distillation Model Inversion Attacks).

2) The proposed DDMI framework obtains notable improvements compared to GMI and LOMMA (GMI) (Table 1), and PLG-MI (Table 3).

3) This work also explores MIAs for CLIP models.

### Strengths
1) This paper is written well and it is easy to follow.

2) The proposed method obtains acceptable improvements over prior methods.

### Weaknesses
1) **Poor selection of baseline methods for comparison in Section 4.2.** GMI is a relatively older work (although it lays foundation for modern generative MIAs) and generally has poor MI accuracy.

- Authors should consider using more advanced baselines such as KEDMI/ LOMMA+KEDMI / PLGMI for SOTA comparison in Table 1.

2) **No empirical evidence/ theoretical grounds for strong claims made in Section 3.1.** Specifically, it is unclear how the authors arrive at the statement, “We attribute these limitations to inherent flaws in GANs” in the context of MIAs.

- Such claims are strong and need clear theoretical or empirical support. Additionally, this statement conflicts with the results reported in the SDM-based vs. StyleGAN-based generative CLIP inversion (Page 10).

- The claim about unstable optimization under GAN-based MIAs requires careful study. The qualitative results shown in Fig. 1(a) alone are insufficient. It would be helpful to explore whether this instability is due to the generative model's architecture, the training objective, the data, or the model quality. One approach to examine this further is to use a checkpoint of the one-step diffusion model with a comparable FID to the GAN, then reproduce Fig. 1(a). This could provide more clarity on the claim.

3) **User studies are necessary to show the quality of privacy reconstruction.** Since this work focuses on private data reconstruction, especially highlighting fidelity, it is important to conduct user study to understand the improvements (See [A, B]).

4) Error bars/ Standard deviation for experiments are missing.

5) In Supplementary D, authors should consider including LOKT [A], as it is the state-of-the-art label-only MIA and significantly outperforms BREP-MI.


Minor:

Table 1 VGG16 w/SDM / CelebA top5 accuracy arrow should be $\uparrow$.

=============

[A] Nguyen, Bao-Ngoc, et al. "Label-only model inversion attacks via knowledge transfer." Advances in Neural Information Processing Systems 36 (2024).


[B] [MIRROR] An, Shengwei et al. MIRROR: Model Inversion for Deep Learning Network with High Fidelity. Proceedings of the 29th Network and Distributed System Security Symposium.

### Questions
Overall I enjoyed reading this paper. But in my opinion, the weaknesses of this paper outweigh the strengths. But I’m willing to change my opinion based on the rebuttal. 


Please see Weaknesses section above for a list of all questions.


======

Post-rebuttal

Thank you authors for the extensive rebuttal and performing additional experiments. I have read all the reviews and the rebuttal. The rebuttal addresses some of my concerns (PLGMI, Error bars for experiments, clarification reg. the use of inversion-specific GANs in the proposed framework). I acknowledge the notable performance gains achieved using your proposed framework and it can be valuable to the community. However, the core questions still remain as acknowledged by the authors in the rebuttal (No empirical evidence/ theoretical grounds for strong claims in Sec 3.1, user studies).

Therefore, I’m afraid I’m unable to increase my rating, as I feel the paper is not ready for publication in its current form. I have suggested some directions for improving Section 3.1 (See my review). Another way to think more deeply about this problem is as follows: **Model inversion attacks aim to search for high-likelihood samples under a target identity. Why, then, does your proposed framework yield significantly better results in this search compared to existing methods? Investigating these questions could provide a more rigorous analysis and a deeper understanding of your framework.**

Overall, this work has good potential, and I wish you the best as you continue to refine it. I also encourage you to address high-resolution MIAs, as suggested by other reviewers.

Thanks again for the extensive rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The study explores generative model inversion attacks (MIAs) using diffusion models to address the limitations of GAN-based inversion attacks. These limitations include instability during the optimization process and low fidelity in reconstructed samples. By incorporating a single-step generator distilled from pretrained diffusion models, the paper presents a novel framework termed Diffusion Distillation MIAs (DDMI). This approach is applied not only to traditional classification models but also to the multimodal CLIP models, uncovering significant privacy risks.

### Strengths
1. Extending MIAs to explore privacy leakage in CLIP models marks a significant original contribution, venturing into an area that has not been extensively studied before. This application highlights the inherent privacy risks in large-scale multimodal models and sets a precedent for future research in this domain.

2.The paper successfully demonstrates that DDMI outperforms traditional GAN-based methods in achieving higher fidelity and stability during the inversion process.

### Weaknesses
1. In my opinion, "Distill the Multi-Step Diffusion Model into a Single-Step Generator" has no much innovation, similar to other One-step Diffusion papers.

2. The paper could benefit from including a broader array of evaluation metrics that could capture other aspects of model performance and attack effectiveness, such as computational efficiency, robustness to adversarial defenses, or qualitative user studies.

### Questions
1. In the experiments, why is there no comparison of computational overhead between gan-based and diffusion-based methods?

2. Why there is no analysis of the robustness of adversarial defenses in the experiment or varience experiment?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a novel model inversion attack with single-step diffusion models. It highlight the instability and low visual fidelity of GANs in MIAs and propose to use diffusion models to overcome the issue. The attackers train a generator distilled by the diffusion model instead of directly training a GAN. The technique can strengthen existing attack methods such as GMI. Moreover, the paper firstly conducts a model inversion research on the multi-modal field, exploring the attacks in CLIP models.

### Strengths
+ The paper use a pre-trained diffusion model to distill a generator, which enhance the stability and the fidelity of the reconstructed images.
+ The paper is the first to explore privacy leakage on large-scale CLIP models leveraging MIAs.

### Weaknesses
+ The method of distilling a single-step generator has been extensively studied in prior work, which limits the novelty of this research. The DDMI approach primarily applies the diffusion distillation technique to model inversion attacks without introducing significantly new ideas.

+ The new investigation for CLIP model inversion is non-sense. First, the numerical results are so weak to prove the urgency of privacy security and the visual results is good mainly due to the inherent ability of the generator, lacking essential experiments for more convincing evidence. Nonetheless, the proposed method does not perform better than StyleGAN-based generative CLIP inversion, which means no superiority. According to the explanation for low performance, more improvement and evaluation should be made to support the research of CLIP model inversion.

+ The experimental results are not sufficient. In Table 1, the classical methods PPA [1], KEDMI [2], PLGMI [3] and LOMMA(KEDMI) [4] are not compared. For target models, the series of ResNet [5] models are usually evaluated in the previous methods, which should be included in the experiments. In addition, there is a lack of comparison with StyleGAN in experimental settings other than CLIP.

+ The experiment setup is too weak. For example, dividing CelebA into public and private parts is a quite easy scenario with low distributional shift, where PLGMI can achieve nearly 99% accuracy. Investigation on such scenario is non-sense to prove the superiority of your method, much less the insignificant improvement compared with LOMMA. Moreover, the division of CelebA is not introduced in this paper. 

+ The experiments of defenses in Table 6 shows that the attack results are worser than the case without SDM with the BiDO defense.

[1] Struppek L, Hintersdorf D, Correia A D A, et al. Plug & play attacks: Towards robust and flexible model inversion attacks[J]. arXiv preprint arXiv:2201.12179, 2022.

[2] Si Chen, Mostafa Kahla, Ruoxi Jia, and Guo-Jun Qi. Knowledge-enriched distributional model inversion attacks. In ICCV, 2021.

[3] Yuan X, Chen K, Zhang J, et al. Pseudo label-guided model inversion attack via conditional generative adversarial network[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2023, 37(3): 3349-3357.

[4] Nguyen N B, Chandrasegaran K, Abdollahzadeh M, et al. Re-thinking model inversion attacks against deep neural networks[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023: 16384-16393.

[5] He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 770–778 (2016)

### Questions
According to the ablation study, the prior loss specified in your method brings negative improvement. Why do you keep this innovation point in your method?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on the advancement of generative model inversion attacks (MIAs). It substitutes the GAN prior with a single-step generator distilled from a pretrained multi-step diffusion model. Besides, this paper first explores CLIP model inversion. Experimental results demonstrate the enhanced performance compared to baselines.

### Strengths
+ **Good Writing**: The paper is well-structured and easy to follow.
+ **New Scenario**: The paper explores a new scenario of CLIP model inversion.

### Weaknesses
+ There are two “Sec.3.1” on the 243~244 lines.
+ The specific expression of $\mathcal{L}_{distill}$ in formula 8 is not explained in the paper.
+ There is a lack of high-resolution comparisons with the two attack methods, including Mirror [1] and PPA [2].

[1] An, Shengwei, et al. "Mirror: Model inversion for deep learning network with high fidelity." *Proceedings of the 29th Network and Distributed System Security Symposium*. 2022.

[2] Struppek, Lukas, et al. "Plug & play attacks: Towards robust and flexible model inversion attacks." *arXiv preprint arXiv:2201.12179* (2022).

### Questions
The trend in Fig 1(a) seems similar between lines. More explanation is expected.

### Soundness
2

### Presentation
3

### Contribution
3
