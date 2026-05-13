# Animate-X: Universal Character Image Animation with Enhanced Motion Representation

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Character image animation, which generates high-quality videos from a reference image and target pose sequence, has seen significant progress in recent years. However, most existing methods only apply to human figures, which usually do not generalize well on anthropomorphic characters commonly used in industries like gaming and entertainment. Our in-depth analysis suggests to attribute this limitation to their insufficient modeling of motion, which is unable to comprehend the movement pattern of the driving video, thus imposing a pose sequence rigidly onto the target character. To this end, this paper proposes \method, a universal animation framework based on LDM for various character types (collectively named \texttt{X}), including anthropomorphic characters. To enhance motion representation, we introduce the Pose Indicator, which captures comprehensive motion pattern from the driving video through both implicit and explicit manner. The former leverages CLIP visual features of a driving video to extract its gist of motion, like the overall movement pattern and temporal relations among motions, while the latter strengthens the generalization of LDM by simulating possible inputs in advance that may arise during inference. Moreover, we introduce a new Animated Anthropomorphic Benchmark (\benchmark) to evaluate the performance of \method on universal and widely applicable animation images. Extensive experiments demonstrate the superiority and effectiveness of \method compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work presents an animation framework capable of animating anthropomorphic characters, along with an accompanying benchmark for animated anthropomorphic characters. Specifically, the framework introduces an Implicit Pose Indicator and an Explicit Pose Indicator to provide rich pose guidance.

### Strengths
1. The visual results of Animate-X demonstrate notable improvements across various characters compared to existing animation methods.
2. Comprehensive experiments and ablation studies are presented.

### Weaknesses
1. No video samples from A2Bench are provided; only selected frames are shown in the paper. Given that the generated videos still struggle with maintaining strict logic and good spatial and temporal consistency, I question the rationale for using T2I + I2V to generate benchmark videos. Specifically, the temporal coherence of the generated videos is unclear, and the method's ability to handle complex motion is not well demonstrated. The benchmark also lacks detailed information, such as video length, frame rate, and the specific parameters used for the T2I and I2V models. Were any additional motion prompts used to generate videos from images? If so, what is their diversity and complexity, and how do these prompts influence the benchmark's overall quality and reliability?
2. The necessity of a pose pool and the selection of an anchor pose image need clarification. What operations are involved in the "align" process, specifically regarding translation and rescaling? The paper does not specify the exact mathematical transformations or the rationale behind choosing a specific anchor pose. Why not use random translation and rescaling instead of relying on an anchor pose image? The current approach seems overly complex and lacks a clear justification for its design choices. It is unclear how the anchor pose is selected and what criteria are used to ensure its suitability.
3. The effectiveness of the Implicit Pose Indicator (IPI) is also in question. The motivation for the IPI is that sparse keypoints lack image-level details, while IPI aims to retrieve richer information. However, Tables 7 and 8 indicate that Animate-X achieves comparable performance to Animate-Anyone and UniAnimate on human videos. This suggests that the IPI does not provide any benefits for human animation, and its contribution to the overall performance is not clearly demonstrated. The paper needs to provide more evidence that IPI is beneficial, especially for the target domain of anthropomorphic characters.

### Questions
Please address the concerns in the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on the animation of non-human characters, addressing two main issues:
1)Sole pose skeletons lack image-level details.
2)Pose alignment in the self-driven reconstruction training strategy.
To resolve these issues, the paper introduces a Pose Indicator, comprising an Implicit Pose Indicator and an Explicit Pose Indicator. Experimental results demonstrate that the proposed Animate-X achieves effective performance in character animation.

### Strengths
1.The authors introduce  A2Bench, which is helpful for the evaluation of character animation.
2.Both qualitative and quantitative experiments are conducted to evaluate the performance of the proposed method.

### Weaknesses
1.Some parts of the writing can be quite confusing, words and sentences are bad orgnized. For example, in P5 L260, what exactly is in the pose pool? And how is it aligned with the reference?
2.The dataset includes 9,000 independently collected videos. Could you analyze these videos, and did other baselines use the same data for training? If not, could this lead to an unfair comparison?
3.The authors first identify the weaknesses of previous methods as a conflict between identity preservation and pose control. They further expand on this point by highlighting two specific limitations: the lack of image-level details in sole pose skeletons and pose alignment within the self-driven reconstruction training strategy. However, while the authors clearly state that differences in appearance between characters and humans can negatively impact animation, learning image-level details seems to contradict their viewpoint  "sole pose skeletons lack image-level details", making this contribution appear more like a forced addition.
4.Additionally, the visualization in Figure 7 provided by the authors also supports w3. The inclusion or exclusion of the IPI appears to have minimal impact on the motion of the Ref image, and with IPI, part of the foot in the Ref image is even missing. This raises doubts about the effectiveness of the IPI module and seems inconsistent with the authors' stated motivation.
5.Pose augmentation has already been widely explored in existing methods, such as MimicMotion, which makes the innovation in this paper insufficient.
6.This paper lacks comparisons with similar methods, such as MimicMotion, which makes the experimental results less convincing.
[1]MimicMotion: High-Quality Human Motion Video Generation with Confidence-aware Pose Guidance

### Questions
See Weakness. If the authors can address all my concerns, I am willing to raise the score.

### Soundness
2

### Presentation
2

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
This paper highlights that character animation models trained exclusively on human-only datasets struggle to learn motion patterns from driving videos, often leading to overfitting on the driving pose and poor generalization to anthropomorphic characters.

To address this issue, the authors propose a novel character animation framework called Animate-X, which incorporates two Pose Indicators. The Implicit Pose Indicator extracts motion and integrates it with CLIP features, while the Explicit Pose Indicator supports an augmentation pipeline during training that encourages the model to learn motion from misaligned pose sequences.

Additionally, a new benchmark is established for evaluating anthropomorphic characters. Experiments across multiple datasets demonstrate the effectiveness of the proposed method for animating anthropomorphic characters.

### Strengths
- The paper introduces a new augmentation method that enhances pose robustness for character animation techniques.
    
- A novel module is proposed to integrate the driving pose with the reference image without relying on a reference network.
    
- A new benchmark is established for evaluating anthropomorphic characters.
    
- The quality of animation results is good, even reference characters do not have leg or arm.

### Weaknesses
 - The paper lacks a detailed analysis of the construction of the augmentation pool, making it difficult to reproduce the method.
    
- There is insufficient in-depth analysis of the model design, such as why the Implicit Pose Indicator (IPI) outperforms the reference network, which has more learnable parameters.
    
- Most styles in the A2Bench benchmark are "3D render style"; the benchmark should include a wider variety of visual styles.

### Questions
- Could the authors provide more details on the construction of the pose pool and alignment pool, such as the pool sizes and how poses are selected from the training set?
    
- Comparing the results in Table 4 and Table 1, Animate-X outperforms the baselines even without pose augmentation (EPI). Could the authors provide a deeper analysis of why the Implicit Pose Indicator (IPI), with fewer parameters, outperforms the reference network?
    
- What happens if the reference pose differs significantly from the candidates in the pose pool and alignment pool? The authors should provide a robustness analysis for this scenario and consider adding a difficulty level split for A2Bench.
    
- Could aligning the driving pose to a "standard" one in the pose pool further improve generation quality?
    
- In the supplementary materials, the authors show results in various styles, yet most styles in A2Bench are in "3D render style." Would it be possible to add a "style trigger word" in the prompt template to diversify and strengthen the benchmark?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed Animate-X, a universal animation framework based on diffusion models. The key insight of this work is that existing image animation frameworks are only focused on the human images and fail to extract the movement pattern of the driving video, leading to the rigid retargeting of the driving pose to the target reference image. The authors propose two pose indicators to address this issue, which can capture comprehensive motion patterns from the driving video. The implicit pose indicator helps retrieve relevant features from the driving video, while the explicit one simulates the unaligned driving poses in the inference stage. To evaluate the approaches, the authors also propose a new benchmark which contains in-the-wild and unmatched driving sequence/reference image pairs. Experiments show that the proposed method outperforms state-of-the-art methods.

### Strengths
1. The motivation of this work is clear, it comes from an in-depth analysis of the failure cases of existing works. The alignment between the driving signal and reference image is critical to the fidelity of character animation. The authors propose an effective method to tackle this problem.
2. The experimental results, especially the video results, are reasonable and interesting. The proposed method shows state-of-the-art performance and outperforms baselines in animating in-the-wild characters. This indicates that the training data is well utilised and shows that the proposed method helps improve the generalisation ability of the animation model.
3. The evaluation benchmark is valuable to the research community. It can help follow-up works measure their methods comprehensively.

### Weaknesses
1. The backbone of this work remains unchanged, it is quite similar to the prior works like your reference AnimateAnyone and MagicAnimate, which makes this work a straightforward extension of existing works and thus reduces the contribution of this paper.
2. Leveraging driving videos to boost the animation performance has been already explored in a few prior works like [1]. The implicit pose indicator is also a similar design which aims to extract comprehensive motion patterns to improve the animation performance.
3. The explicit pose indicator is a little bit confusing because I think this module is an augmentation of the driving pose sequences. Therefore, the novelty of the proposed method is not very significant. It is reasonable that the augmentation can break the strong correspondence between the driving video and motion representation. What is the advantage of this training time rescale augmentation and over the test time pose alignment? Are there any ablation studies about this?
4. From the results of the animation of anthropomorphic characters, the example of a banana shows that although the animation result looks like a banana, the motion precision is decreased. Therefore, I think the implicit pose indicator could harm the motion precision. The authors could conduct more experiments to study this issue.

### Questions
Does this model still use any input videos in the inference stage? I am asking this question because there are no input driving videos in the “Animating anthropomorphic characters” section of the supplementary materials. Could the author explain the inference setting? If there is a corresponding driving video, it is better to also include them into the results.

### Soundness
3

### Presentation
3

### Contribution
3
