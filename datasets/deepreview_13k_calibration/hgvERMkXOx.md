# Watch Less, Do More: Implicit Skill Discovery for Video-Conditioned Policy

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
In this paper, we study the problem of video-conditioned policy learning. While previous works mostly focus on learning policies that perform a single skill specified by the given video, we take a step further and aim to learn a policy that can perform multiple skills according to the given video, and generalize to unseen videos by recombining these skills. To solve this problem, we propose our algorithm, Watch-Less-Do-More, an information bottleneck-based imitation learning framework for implicit skill discovery and video-conditioned policy learning. In our method, an information bottleneck objective is employed to control the information contained in the video representation, ensuring that it only encodes information relevant to the current skill (Watch-Less). By discovering potential skills from training videos, the learned policy is able to recombine them and generalize to unseen videos to achieve compositional generalization (Do-More). To evaluate our method, we perform extensive experiments in various environments and show that our algorithm substantially outperforms baselines (up to 2x) in terms of compositional generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Watch-Less-Do-More (WL-DM), an imitation learning framework for video-conditioned policy learning, to enable an agent to learn multiple skills from videos and generalize to unseen task combinations. The method uses an information bottleneck to implicitly discover skills and decompose video demonstrations into tasks without requiring explicit video segmentation annotations. WL-DM is evaluated in environments like Frank Kitchen and MetaWorld, demonstrating its capacity to achieve compositional generalization in unseen task combinations, outperforming baseline methods.

### Strengths
- The article is clearly written and proposes an effective solution to the problem of skill discovery without relying on language information or manual annotation.

### Weaknesses
1. There lack of comparative experiments on learning directly from the segmented sub-task videos, so it is hard to see whether the method achieves its intuition of *Focusing on the current task*.
2. In potential real-world applications, the various steps in multi-step tasks are often causally linked, and the appearance of the same task in different videos may be different. Additionally, the accessible training videos are not guaranteed to cover all elements in downstream tasks, without including elements out of a certain task set. As a result, the generalizability of the method appears to be somewhat limited for now.

### Questions
1. Is there any ablation about the number of videos in the training set? This includes how many types of task combinations there are, and how many videos with different initializations are there for each combination.
2. How similar do two video clips from different training videos need to be to be considered as the same task?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method to train video-conditioned policies, which employ an information bottleneck-based objective to learn a video encoder for implicit skill discovery. The proposed method is novel, and the experiments on both Frank Kitchen and MetaWorld demonstrate its performance outperforms baselines.

### Strengths
- Learning an executable policy from videos is a good topic, since video is a general interface across different domains and there are widely available video data. This paper further proposes an information bottleneck-based imitation learning framework for implicit skill discovery and video-conditioned policy learning, which is novel and sound.
- Good writing and clear motivation. This paper derives its final objective from both skill discovery and information bottleneck perspectives.
- Experiments on both  Frank Kitchen and MetaWorld demonstrate its superior performance.

### Weaknesses
 - The baselines compared in this paper are not originally video-conditioned. DT is proposed to be conditioned on states, and VIMA is conditioned on texts and images. I encourage the authors to include a video-based baseline to strengthen this paper.


### Questions
- What is the generalization ability of your proposed method? Can it generalize to unseen tasks or unseen visual backgrounds? This is an important factor which should be investigated.

### Soundness
3

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
4

### Summary
The paper proposes an information bottleneck-based imitation learning framework, WL-DM (Watch-Less-Do-More), for implicit skill discovery and video-conditioned policy learning. This strategy can generalize to unseen video task combinations, demonstrating strong compositional generalization ability. The idea of implicit skill decomposition is innovative, especially in achieving task segmentation within videos without requiring explicit video segmentation annotations.

### Strengths
This paper proposes that the WL-DM framework innovatively employs an information bottleneck approach for implicit skill discovery, allowing effective task segmentation without explicit annotations. The method demonstrates strong compositional generalization, successfully adapting to unseen video task combinations.

### Weaknesses
1. The compositional generalization seems limited to combining different tasks, while in practice, different task combination sequences will not have different effects on similar outcomes. Could the authors clarify the practical significance of this generalization with examples of real-world scenarios where it proves valuable or challenging?

2. The paper claims that video-conditioned policies can achieve combinatorial generalization when tasks can be performed independently. Could you explicitly compare WL-DM to single-task learning methods and clarify which mechanisms in WL-DM enable combinatorial generalization beyond what single-task approaches offer?

3. The paper lacks an experimental comparison with skill-based imitation learning methods (e.g., Xu et al., 2023; Wang et al., 2023; Shin et al., 2023; 2024) and single-task video demonstration methods (e.g., Chane-Sane et al., 2023). Could the authors analyze specific performance metrics, such as generalization ability or data efficiency, to provide a more detailed comparison with these methods?

4. The experimental results are relatively limited, such as lacking empirical support for the advantages of implicit segmentation, as well as necessary visualizations or other forms of demonstrations to validate the effects of implicit segmentation.

### Questions
1. what is the practical significance of compositional generalization?

2. Can the author analyze the performance of the above paper methods in the experiment?

3. Can the author provide more experimental results to verify the effectiveness of the model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Watch-Less-Do-More (WL-DM), an imitation learning framework designed for video-conditioned policy learning that aims to enhance compositional generalization. WL-DM uses an information bottleneck method to identify relevant skills from videos, allowing the policy to handle complex, unseen video task combinations by focusing only on current tasks. Experimental results across two robotic environments (Franka Kitchen and Meta World) show WL-DM surpassing baseline models in generalization ability. The authors also highlight the potential for broader applications, though they note limitations regarding video data alignment with task segmentation.

### Strengths
- The framework is sound, well-structured, and novel.
- The overall content is easy to understand and well-written.

### Weaknesses
 - It would be beneficial to clearly explain the difference between the proposed method and various existing approaches that use mutual information for skill extraction [1, 2, 3].
- There are questions regarding the appropriateness of the chosen baselines. The authors used VIMA as the SOTA baseline, but VIMA showed very low performance. They suggest that this may be due to VIMA's reliance on multi-modal data, which could degrade performance when using only pure video data. However, a comparison with other one-shot imitation methods that use only video data would provide a more relevant evaluation.

### Questions
- For mutual information loss, the importance might vary depending on the diversity and length of skills in the environment. Should it be adjusted according to each environment? If so, how should it be approached?
- Could you show how the skills were separated in the experiments conducted? Do similar z-values actually appear consecutively, allowing the skills to be segmented?
- Additionally, providing a visual representation of whether the skill space is discretely separated into a minimal set of skills when using this type of loss would aid the reader’s understanding.

### Soundness
3

### Presentation
2

### Contribution
2
