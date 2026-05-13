# Conditional density estimation for video prediction with score-based models

- Decision: Reject
- Scores: 6, 5, 1, 1

## Abstract
Temporal prediction is inherently uncertain, but representing the ambiguity in natural image sequences is a challenging high-dimensional probabilistic inference problem. For natural scenes, the curse of dimensionality renders explicit density estimation statistically and computationally intractable. Here, we describe an implicit regression-based framework for learning and sampling the conditional density of the next frame in a video given previous observed frames. We show that sequence-to-image deep networks trained on a simple resilience-to-noise objective function extract adaptive representations for temporal prediction. Synthetic experiments demonstrate that this score-based framework can handle occlusion boundaries: unlike classical methods that average over bifurcating temporal trajectories, it chooses among likely trajectories, selecting more probable options with higher frequency. Furthermore, analysis of networks trained on natural image sequences reveals that the representation automatically weights predictive evidence by its reliability, which is a hallmark of statistical inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a simplified diffusion-based framework for modeling conditional density, with demonstrations in video prediction. The key idea, derived from the empirical Bayes formulation of score-based models, involves learning a denoising function that implicitly infers noise levels and removes noises of arbitrary magnitude from an input. This denoiser yields an estimation of a family of score functions across noise levels. This framework thus removes the time axis in a standard diffusion model, and pursues a direct regression approach, allowing easy analysis of the learned representations. This framework is evaluated on synthetic videos, as well as natural image sequences.

### Strengths
The main contribution of this paper is mostly conceptual. The key ideas of (1) employing a direct regression approach for learning score-based models and (2) the sampling strategy from the learned denoising function are both intriguing. It is perhaps a bit surprising to see how they can work even on some toy data. 

The proposed framework presents an interesting and significantly simplified alternative to existing diffusion models.

The paper is well-written overall. The results, including a detailed analysis of the learned representations, are elaborated.

### Weaknesses
Despite the conceptual novelty, the practicality of the proposed framework is somewhat questionable. Considering the problem of video prediction, it is probably fair to say that the proposed framework provides at best an alternative solution to diffusion models. While diffusion models have demonstrated impressive results for video generation and prediction, the proposed framework is solely demonstrated on “toy” data (small scale, low resolution synthetic and real videos). It is not clear if the proposed framework can scale up to larger datasets or higher resolution videos. The paper lacks a rigorous comparison to existing video prediction methods, making it difficult to assess its relative performance. The analysis of the learned representations, while interesting, does not provide a clear advantage over existing methods, and it is not clear how these representations could be used for downstream tasks. Furthermore, the paper does not discuss the computational cost of the proposed method, which is a critical factor for practical applications.

### Questions
It will be very helpful to include a discussion that draws the boundary between the proposed framework and well-known diffusion models.

A demonstration of the proposed framework on high resolution videos will help to strengthen the experiments. If this is not possible, a discussion about the scalability might be beneficial.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript formulates probabilistic forecasting of the next video frame as a generative modeling task. The proposed method allows to recover plausible instances of the next frame by iteratively sampling a denoising deep generative model through Tweedie's formula. In the experiments, the denoising model is a U-Net with up to \tau=2 conditioning frames. The model optimizes the L2 reconstruction loss which corresponds to log p(x|y,c). The experiments have been performed on a synthetic dataset (moving leaves) and DAVIS32.

### Strengths
- forecasting future frames in video is an important problem
- generative modelling is an appropriate tool for the task at hand due to ability to account for multimodal future

### Weaknesses
 - the proposed method appears quite straight-forward and in line with previous recent work in the field
[a] Gabriel Loaiza-Ganem, Brendan Leigh Ross, Luhuan Wu, John P. Cunningham, Jesse C. Cresswell, Anthony L. Caterini. Denoising Deep Generative Models. ICBINB 2022

- the manuscript does not report quantitative comparison with related work in the field; for instance, it would be insightful to report MS-SSIM and LPIPS on Cityscapes and KITTI, as in [b] and references therein.
[b] Yue Wu, Qiang Wen, Qifeng Chen. Optimizing Video Prediction via Video Frame Interpolation. CVPR 2022: 17793-17802.

- equation (1) is not clear due to index s having two distinct roles (also, it would be helpful to clarify whether s>t is feasible)
- it would be good to clarify whether f(y,c) is E[x|y,c] as in (2) or f(y,c) is E[x|y,c] - y as in (7)

### Questions
- equation (1) is not clear due to index s having two distinct roles (also, it would be helpful to clarify whether s>t is feasible)
- it would be good to clarify whether f(y,c) is E[x|y,c] as in (2) or f(y,c) is E[x|y,c] - y as in (7)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper describes a probabilistic formulation for next-frame-prediction.  The paper develops statistical machinery based on learned denoising functions in what appears to be a sampling approach, although the details are vague and hard to follow.  The method is tested on a synthetic, procedural dataset and a small natural image sequence dataset.

### Strengths
- The paper motivates a strong problem about the lack of transparency in next-frame generation (or general video generation) papers.
- The base formulation for the next prediction is sound.

### Weaknesses
 - The development of the technical ideas in the paper are difficult to follow, moving from an initial problem formulation to denoising without any reasonable discussion.   Then the discussion jumps around with relatively basic statistical machinery without giving any details of the actual method.   Better description of what the novelty in the method would be helpful.  More concrete relationship between the current work and the related art is very important to help the reader understand the current method and its contributions.

- The overall approach seems similar to other probabilistic generative methods, even those noted in the paper.

- The evaluation approach is not well described or convincing.  There are not comparisons to component methods or baselines.  It would improve the paper if comparative baselines were included.  The notion of occlusion, which may be useful is introduced seemingly out of nowhere.  It would improve the paper if there is more discussion motivating this evaluation.  However, evaluation should also describe general generation techniques.  The natural image sequences tested are few.  It would improve the paper to demonstrate capability on establish video generation benchmarks with established video generation evaluation protocols, beyond PSNR.  The details of the networks used are unclear.  It would improve the paper to have a thorough network description, even if in the appendix.

- (Minor) Typos exist in the paper; e.g., line 89 focuese

### Questions
- The temporal sampling of an image sequence is an artifact of the technology; how does this impact the modeling proposed.  The basic technical premise is disarming: "The next frame in an image sequence is a single event with several possible outcomes..."  The next frame in an image sequence has very very many possible outcomes; it's also not clear what "an event" means (in the context of the earlier part of this bullet).  It would be helpful if the paper included a discussion of the impact of this discrete sampling of continuous time along with a discussion of the potential impact this has on the method's performance.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
The paper proposes a score-based model for conditional density estimation tailored to video prediction. The authors demonstrate that single-step denoising results in blurred predictions, highlighting the necessity of iterative denoising—a standard approach in score matching, diffusion, and flow matching models—to capture sharper, more plausible outcomes. Through a straightforward dataset and network, they further illustrate the distinct contributions of past frames and the current noisy frame in shaping accurate predictions.

### Strengths
The paper defines score matching formulation for video prediction in a really accurate way. They also show how adding noise is helpful both in training and inference.

### Weaknesses
It’s challenging to identify the novel contribution of this paper, as it seems to be positioned somewhat independently, with limited engagement with prior work on video prediction, particularly with diffusion models. More explicit connections to existing approaches and an analysis of what this model uniquely offers in comparison would strengthen the work. The paper's analysis of the network's adaptive behavior, while interesting, is not thoroughly explored. The local linear analysis provides only a partial view of the learned representations, and it's unclear how this analysis advances our understanding of video prediction models beyond what is already known. The description of the score-based framework, while accurate, does not sufficiently highlight its advantages over existing methods, particularly in terms of computational efficiency or prediction quality. The authors should provide a more detailed comparison to establish the practical benefits of their approach.

### Questions
Could the authors clarify how their approach to conditional density estimation for video prediction differs from existing score-based or diffusion models?

What specific insights or improvements does this work offer over current state-of-the-art methods in video prediction?

How does the analysis of the network's adaptive behavior contribute to our understanding of video prediction models?

### Soundness
4

### Presentation
4

### Contribution
1
