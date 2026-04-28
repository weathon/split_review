# A Closer Look at Backdoor Attacks on CLIP

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
We present a comprehensive empirical study on how backdoor attacks affect CLIP by analyzing the representations of backdoor images. Specifically, based on the methodology of representation decomposing, image representations can be decomposed into a sum of representations across individual image patches, attention heads (AHs), and multi-layer perceptrons (MLPs) in different model layers. By
examining the effect of backdoor attacks on model components, we have the following empirical findings. (1) Different backdoor attacks would infect different model components, i.e., local patch-based backdoor attacks mainly affect AHs, while global noise-based backdoor attacks mainly affect MLPs. (2) Infected AHs are centered on the last layer, while infected MLPs are decentralized on several late layers. (3) Some AHs are not greatly infected by backdoor attacks, and even infected AHs could still maintain the original functionality. These observations motivate us to defend against backdoor attacks by detecting infected AHs, repairing their representations or filtering backdoor samples with too many infected AHs, in the inference stage. Experimental results validate our empirical findings and demonstrate the effectiveness of the defense methods

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides an analysis of how backdoor attacks affect the CLIP model. The paper focuses on the behavior of image representations at various parts of the model. The paper decomposes CLIP’s image representations to understand the effect of backdoor attacks on CLIP's individual components - attention heads and MLPs. 
The paper shows:
1. Different backdoors affect different model components.
2. Affected AHs are localized to a specific region within the layer, whereas affected MLPs are spread-out.
3. AHs are affected to varying degrees of infection.

### Strengths
1. This paper sets a good example of how adversarial attack analysis should be done. They conduct well defined analysis of different backdoor attacks on the architectural components of CLIP. This reveals potential component-level vulnerabilities of CLIP-based and attention-based multi-modal architectures.
2. The authors demonstrate a strong understanding of math and technical knowledge. This is shown by the comprehensive breakdown of the analysis with respect to multiple backdoor attacks and differentiating between local and global trigger types. Further, the paper also shines light  on how distinct attacks interact with specific layers and components. 
3. The authors have performed comprehensive experimentation and substantiated their claims with quantitative results. The authors also conduct a sufficient ablation study. 
4. The paper's language and style of writing is easy to understand.
5. Lastly, the paper's contributions are certainly relevant to the adversarial and multi-modal community. This paper also demonstrates which layers pay attention to what in an image. Although this may seem as known knowledge or more like an explainability experiment, this paper provides important information that can be used to craft targeted attacks and stronger detection and defense techniques to counter other adversarial attacks and not just backdoors.

### Weaknesses
1. In conjunction with strength 3, I will note that although the experimentation is extensive, the authors do not do a good job of explaining the results or giving readers a better understanding of what the experiments show. The authors could have gone into more detail about what the results show; For example: could have provided a sample input image, various versions of the backdoored image and then shown the AHs and MLP's attending to different triggers differently. This could have drive home their claim and visually strengthened their analysis.
2. For a more thorough ablation study, the authors could maybe experiment with varying architectures, or modified existing networks to change layer orders to understand whether their claims such as "Infected AHs are centered on the last layer" are indeed due to certain trigger/attack-based factors rather than architectural reasons.
3. In conjunction with strength 4, although the paper's language is lucid, the math hamper's readability. The authors could supplement their use of math with textual explanation of what the math intuitively explores; For example in section 'Repairing representations of infected AH' or 'Preliminary'. It may help to boil down equations to only necessary parts that are directly relevant to reader's understanding.
4. Although the paper's experimentation is extensive, the authors could have incorporated stronger attacks like dynamic triggers ('Reflection Backdoor', 'Hidden Trigger Backdoor Attacks') and patch-based triggers with adaptive patterns ('Input-Aware Dynamic Backdoor Attack').

### Questions
1. The authors fail to address the applicability of their analysis to non-CLIP based multi-modal and attention-based models. Is it the case that the findings translate over to these other models. If they do, then do location based claims like "Infected AHs are centered on the last layer" still hold true? If not, then why?

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
This paper examines the impact of backdoor attacks on CLIP by analyzing the representations of backdoor images using a representation decomposing methodology. Three key findings are presented regarding the influence of backdoor attacks (local-patch and global-noise attacks) and network layers (AHs and MLPs). Additionally, the paper proposes countermeasures to repair model components and filter samples to mitigate the effects of backdoor attacks.

### Strengths
The motivation of the paper is clearly articulated, and it extends existing research on backdoor attack methods to different CLIP architectures, which could be a valuable contribution to the backdoor research community.

### Weaknesses
I think there are some issues with this paper, particularly concerning the generality of certain parameters in the CLIP domain and its performance in addressing different types of backdoor attacks.



### Questions
1. The authors categorize backdoor attacks into two types: local-patch based and global noise-based backdoor attacks. To my knowledge, the paper "Input-Aware Dynamic Backdoor Attack" introduces a "dynamic" backdoor, where lots of samples share similar pixels in the backdoor trigger but also share some different backdoor pixels. I am wondering whether this attack yields the same experimental conclusions. Should it be classified as local patch-based or global noise-based type?
2. Finding 3 states, "descriptive texts of MLPs in the last five layers have a distinct semantic difference, while that of MLPs in other layers have negligible changes in semantics." Why specifically the last five layers? Is this conclusion solely based on the experimental results presented in Figure 3?
3. As a defender, how can I determine whether a backdoor type is local patch-based or global noise-based? Additionally, the choice of parameter in Figure 7 seems to struggle to achieve a good balance between attack sucess rate and clean accuracy.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an empirical study investigating how backdoor attacks affect CLIP models by analyzing representations of backdoor images. By examining the effects on different model components (attention heads and MLPs), the paper proposes two defense methods that detect infected AHs, repair representations or filtering samples.

### Strengths
Comprehensive empirical analysis that provides insights into how backdoor attacks affect different components of CLIP.

### Weaknesses
1. Limited novelty in some key findings. The observation that local patch-based attacks mainly affect AHs while global noise-based attacks mainly affect MLPs seems intuitive and somewhat expected.

2. In Figure 2, it is difficult to distinguish the original images. Figure 3, while presenting a lot of descriptive texts, lacks intuitive clarity, making it challenging to draw conclusions directly from it.

3. Defining the threat model at the beginning will make the paper clearer.

### Questions
How would the conclusions hold for semantic triggers rather than simple patches or textures? How might the affected layers change with semantic triggers?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper mainly present an empirical study on the backdoor attacks against the CLIP models. The study revels three observations about the effect of backdoors on different representations of CLIP: 1) different backdoor attacks infect different model components; 2) infected AHs are centered on the last layer while infected MLPs are decentralized on multiple layers; 3) some AHs are not greatly infected by backdoor attacks. Bases on the observations, the authors propose a backdoor defense method by detecting infected AHs.

### Strengths
1. Explore the work pattern of backdoor attacks against CLIP from the perspective of representation decomposing;
2. Propose a potential method to defend against backdoor attacks for CLIP;
3. Doing experiments to validate empirical findings.

### Weaknesses
1. The authors classify the backdoor triggers into two categories, namely local-patch and global-noise, and then, explore their effects against CLIP. Is such a trigger pattern classification generic enough to validate the effectiveness of the revealed findings? For example, current works have achieved multi-trigger (or multi-target) backdoor attacks. According to the author's second finding, the injected multiple triggers should all be centered on the last layer. However, intuitively, if attacker chooses to put the triggers on difference places, their representations can be more like global-noise ones, which is against the author's finds, isn't it? Another example is the triggers that look like natural inputs, which may change the injected neurons. In summary, to make the finding more persuasive, the authors should better give a more comprehensive discussion on the reasonability of the selection of attack types, or provide experiments to prove it.
2. The proposed defense works in two pipelines (against two different attack types), and it looks like that implementing these two pipelines simultaneously is time-consuming. So, how do the defender know which defense pipeline should be selected in practice? Seem to be impossible.
3. A confusing conflict: the 2nd finding says the local-patch backdoor infects AH, while the last finding claims that AHs are not greatly infected? So, are the AHs infected at all? If yes, the last finding seems to be meaningless. If no, what about the correctness of the 2nd finding? By the way, what is the meaning of the last finding? From this manuscript, it seems to have no relation and motivation to derive the final defense method.
4. I really appreciate the efforts of authors to do these experiments to reveal their findings. However, there is no novel approach involved in the study procedure but only invocations of different previous tools. Moreover, the final findings are similar to an early work, i.e., the well-known ''fine-pruning" defenses.

### Questions
1. Is such a trigger pattern classification generic enough to validate the effectiveness of the revealed findings?
2. How do the defender know which defense pipeline should be selected in practice?
3. Please clarify the importance of the last finding with more details.
4. Please clarify the basic difference of the findings compared to the well-known ''fine-pruning" defenses.

### Soundness
2

### Presentation
2

### Contribution
2
