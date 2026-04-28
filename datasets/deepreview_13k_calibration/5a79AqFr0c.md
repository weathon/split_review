# ControlVideo: Training-free Controllable Text-to-video Generation

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Text-driven diffusion models have unlocked unprecedented abilities in image generation, whereas their video counterpart still lags behind due to the excessive training cost of temporal modeling. Besides the training burden, the generated videos also suffer from appearance inconsistency and structural flickers, especially in long video synthesis.
To address these challenges, we design a \emph{training-free} framework called \textbf{ControlVideo} to enable natural and efficient text-to-video generation.    
ControlVideo, adapted from ControlNet, leverages coarsely structural consistency from input motion sequences, and introduces three modules to improve video generation. 
Firstly, to ensure appearance coherence between frames, ControlVideo adds fully cross-frame interaction in self-attention modules. 
Secondly, to mitigate the flicker effect, it introduces an interleaved-frame smoother that employs frame interpolation on alternated frames. 
Finally, to produce long videos efficiently, it utilizes a hierarchical sampler that separately synthesizes each short clip with holistic coherency.
Empowered with these modules, ControlVideo
outperforms the state-of-the-arts on extensive motion-prompt pairs quantitatively and qualitatively.
Notably, thanks to the efficient designs, it generates both short and long videos within several minutes using one NVIDIA 2080Ti.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces "ControlVideo," a training-free framework that significantly improves text-driven video generation. It addresses issues like appearance inconsistency and flickers in long videos through innovative modules for frame interaction and smoothing. ControlVideo outperforms existing methods, efficiently generating high-quality videos within minutes.

### Strengths
•	The proposed method is straightforward, easily implementable, and reproducible, making it accessible for further research and application.

•	The paper introduces novel techniques for long video generation, and the "interleaved-frame smoother" effectively improves frame consistency.

•	The results demonstrate improvements over existing methods, substantiating the paper's claims.

### Weaknesses
•	While the full-attention mechanism and "interleaved-frame smoother" enhance frame consistency, they also significantly increase the computational time. The paper does not provide a detailed analysis of the computational complexity of these modules, making it difficult to assess their practical scalability. A more thorough breakdown of the time cost associated with each component (e.g., attention calculation, smoothing operation) would be beneficial.

•	The background appears to flicker in relation to the foreground in some examples. For instance, in the "James Bond moonwalk on the beach, animation style" video on the provided website, the moon inconsistently appears and disappears. This suggests that the method struggles with maintaining temporal consistency in the background, particularly when the foreground undergoes significant motion or changes. The lack of a robust mechanism to ensure background stability is a notable limitation.

•	The paper lacks quantitative comparisons with Text2Video-Zero in the context of pose conditions, which could be a significant oversight given the importance of pose in video generation. The absence of such comparisons makes it hard to evaluate the method's performance in scenarios where pose control is a critical factor. It is unclear how the proposed method handles complex pose variations and whether it can effectively maintain consistency in these conditions.

### Questions
•	Could you provide additional results for long video generation to further validate the method's efficacy?

•	Is there a potential solution to the flickering background issue mentioned in the second weakness?

•	Would it be possible to employ a non-deterministic DDPM-style sampler as an alternative to DDIM?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes ControlVideo, a training-free framework that can produce high-quality videos based on the provided text prompts and motion sequences (e.g., different modalities). ControlVideo adapts a pre-trained text-to-image model (i.e., ControlNet) for controllable text-to-video generation. The paper introduces an interleaved-frame smoother that alternately smooths out the latents of successive three-frame clips by updating the middle frame with the interpolation among the other two frames in the latent space, aiming to stabilize the temporal continuity of the generated videos. Besides, a fully cross-frame interaction mechanism is exploited to further enhance the frame
consistency, and a hierarchical sampler is employed to produce long videos more efficiently. Experimental results demonstrate that the proposed ControlVideo outperforms the state-of-the-art baselines both quantitatively and qualitatively.

### Strengths
- The paper is clearly written, well organized, and easy to follow. The symbols, terms, and concepts are adequately defined and explained. The language usage is good.

- The proposed method is simple and easy to understand. Sufficient details are provided for the readers.

- The experiments are generally well-executed. The empirical results show the effectiveness of the proposed method, showing certain advantages over state-of-the-art baselines.

### Weaknesses
 - The qualitative results showcase certain advantages of the proposed method over state-of-the-art baselines in controllable text-to-video generation. However, by checking the provided video results, the temporal consistency can still be improved. Also, in some cases, the background looks unchanged. Some visual details can still be improved. Providing more discussions on these could strengthen this paper further.

- The fully cross-frame interaction mechanism considers all frames as the reference, which thus increases the computational burden. What is the intuition to consider all the frames as a large image? Why not select some key frames to reduce redundant information? It is interesting to provide more discussions and analysis on this.

- The paper mentioned that the proposed interleaved-frame smoother is performed on predicted RGB frames at timesteps {30, 31} by default. It can be more interesting if more studies and analyses on different steps to apply such a mechanism are provided.

- It seems the interleaved-frame smoother still brings more computational cost and affects the model efficiency due to the additional conversion and interpolation steps.

### Questions
- Why does the hierarchal sampler improve model efficiency? It seems all the frames still need to be generated, although it is a top-down generation from key frames.

- It is suggested to remove some content about the background and preliminary since such information is well-known.

- The reviewer is interested if the proposed ControlVideo can be extended to generate more challenging new information, such as a novel view/unseen part of an object.

-  Will the authors release all the code, models, and data to ensure the reproducibility of this work?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work focuses on training-free controllable text-to-video generation tasks. It introduces an interleaved-frame smoother method to generate smoother frames. Additionally, it modifies cross-frame interaction to better utilize Stablediffusion's weights, enhancing frame continuity.

### Strengths
- The writing is clear and easy to follow.
- It is a training-free method, not relying on large-scale training, and has low computational resource requirements.
- The ablation experiments are well-designed and easy to understand.

### Weaknesses
 - Overall, the innovation is average; applying ControlNet to video editing or generation is straightforward and easily thought of.
- The experiments are not comprehensive; there are too few baseline comparisons, and the experimental validation is limited to just over 20 examples, making the results less convincing.
- Limited by the absence of structure condition, this method can mainly edit videos with similar motion. Its effectiveness diminishes for videos with different motions or poses.

### Questions
As shown above, despite the method's average innovation and some shortcomings, I believe the exploration in this direction is worthwhile. 
- I hope the authors can complete more experiments and cases, preferably providing an analysis of failure cases. 
- Relying solely on the demo examples provided in the paper makes it challenging to be fully convinced.
- If the authors can address my concerns, I will consider giving a higher score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a trainig-free framework to produce videos based on provided text prompts and motion sequences. An interleaved-frames smoother and a fully cross-frame interaction mechanism with a hierarchical sampler are proposed to enhance the quality of synthesized videos. The authors demonstrate that they achieve sota performance by entensive experiments.

### Strengths
1. The paper is well-written and easy-to-follow. 
2. The proposed method is highly efficient and does not need training at all. Nevertheless, the quality of synthesized videos are not bad.

### Weaknesses
1. The proposed components (inter-frame interpolation, and cross-frame attention) are more-or-less explored in recent works. As such, I'm uncertain if this research will provide substantial insights to the community.

2. The proposed metrics (frame consistency, and prompt consistency) leverage CLIP model. Given that the CLIP model primarily operates in a deeply semantic and abstract domain, it often misses finer image details. Consequently, I'm inclined to think that the suggested metric might not adequately assess temporal consistency (for example, critizing jittering and discontinuity). Thus, the assertion that the proposed methods attain improved temporal consistency seems to lack robust quantitative backing.

3. This training-free framework cannot capture fine-grained motion pattern in video. Therefore, I believe it may not be the optimal approach for producing high-quality video content. Instead, I think finetuning the model on large-corpus video data might help improve the quality.

### Questions
Just as stated in the weakenss section, I am skeptical about the potential of training-free framework in video generation area. I'd be keen to hear the authors discuss potential future research directions in this direction.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
