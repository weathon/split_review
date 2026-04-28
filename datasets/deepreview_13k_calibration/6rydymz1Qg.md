# Efficient Continuous Video Flow Model for Video Prediction

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Multi-step prediction models, such as diffusion and rectified flow models, have emerged as state-of-the-art solutions for generation tasks. However, these models exhibit higher latency in sampling new frames compared to single-step methods. This latency issue becomes a significant bottleneck when adapting such methods for video prediction tasks, given that a typical 60-second video comprises approximately 1.5K frames. In this paper, we propose a novel approach to modeling the multi-step process, aimed at alleviating latency constraints and facilitating the adaptation of such processes for video prediction tasks. Our approach not only reduces the number of sample steps required to predict the next frame but also minimizes computational demands by reducing the model size to one-third of the original size. We evaluate our method on standard video prediction datasets, including KTH, BAIR action robot, Human3.6M and UCF101, demonstrating its efficacy in achieving state-of-the-art performance on these benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presented method to efficiently predict video by reducing number of diffusion steps time and also model size required for generation. The authors considered video as a continuous process and utilized a latent space to interpolate between two consecutive frames. Instead of starting from a static Gaussian distribution for each frame, they started from the last predicted frame. Considering latent space for interpolating between frames reduced latency and improved performance.

### Strengths
- This work addressed an important and hard problem.
- Using latent space for generation sounds effective for reducing latency and improving performance. Which may reduce overall complexity and run time of diffusion models for video prediction task.
- Presented a detailed experimental results.

### Weaknesses
 - Not easy to follow theoretical justifications and derivations in the method section.
- Please refer to "Questions" section.

- lines 165-166, how it allows for a larger context window?
- Please define 't' in line 170, though standard notation.
- Line 177, "Once the frames are encoded", seems like the frames are being encoded all together. Is that so? Then how it is being handled during the reversed process? Reverse process is also using the continuous latent space.
- Please define z^x and z^y. How they are different from  z^j and z^(j + 1)?
- How the error coefficient in Eq. (1) is obtained?
- In line 187, "with latent z_y", should it be z^T?
- Eq. (2) (z_y - z_x) \del t term is not clear to is obtained.
- How \tilde{\mu} is obtained in Eq. 192?

### Questions
- lines 165-166, how it allows for a larger context window?
- Please define 't' in line 170, though standard notation.
- Line 177, "Once the frames are encoded", seems like the frames are being encoded all together. Is that so? Then how it is being handled during the reversed process? Reverse process is also using the continuous latent space.
- Please define z^x and z^y. How they are different from  z^j and z^(j + 1)?
- How the error coefficient in Eq. (1) is obtained?
- In line 187, "with latent z_y", should it be z^T?
- Eq. (2) (z_y - z_x) \del t term is not clear to is obtained.
- How \tilde{\mu} is obtained in Eq. 192?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new approach for video prediction, which is defined as predicting future frames from past context. They model all the frames as one single continous sequence, and aim to predict the next frame as a function of previous one instead of regressing from a latent noise. With two improvements over prior works - working in the latent space and directly modeling frame sequences, they show results on various video prediction benchmarks.

### Strengths
- Handles a very challenging problem of video future prediction.
- New approach, different from prior works on using GANs or pixel-space diffusion.
- Showed results on a variety of challenging benchmarks.

### Weaknesses
 - The forumulation of the solution is not technically convincing. For example, the equation 1 is directly written without any intuition, reference or justification of why this is the most optimum modeling choice. In general, this subsumes a lot of assumptions about motion modeling in real videos and seems generally restrictive to model challenging scenarios like large motion, shot changes, occlusions and pixel-space variations. Since the whole work rests upon this assumption, the authors are requested to provide a better justification of their choice. 

- The experiments can also showcase performance on few special cases like occlusions and large motions and the validity of Eq 1 in these scenarios. 

- In eq 8, it seems like the random variable is $z_{t-1}$, but the RHS contains distribution over $z_t$. Also, in eq3, $g(t) = -t\log t$ might imply potentially negative variance, since $t>1$ leads to $-t \log t<0$. These can be further explained.

### Questions
- Please see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a video generation method (unclear if it is prediction or interpolation) that is structured around a conditional-diffusion-like model but that attempts to be more efficient by structuring the noise process based off of the adjacent frame.  The paper evaluates the method on four video datasets and compares it to the baselines.

### Strengths
- The method is well motivated --- that careful method construction is needed to improve the efficiency of video generation methods.

- The paper incorporates evaluation on multiple video datasets and seems to outperform the relevant methods.

- The paper performs the generation in latent space rather than in pixel space.

### Weaknesses
 - The discussion of the method itself is rather terse and hard to understand.   Examples include challenges with undefined notation, an unclear concrete problem definition, and limited concreteness around the reduction to practice.  This detracts from one's ability to sufficiently understand the results and contextualize them.

- The relationship between classical conditional diffusion and this proposed method needs to be better explained.

- Although the evaluation is rich in terms of datasets used and baselines compared, there is very little actual insight derived from the evaluation?  We do not learn any notion of why the method may be working better than the baselines.  We do not learn any insight into the details of the method setup and its impact to the performance?  Fewer datasets and more analysis would be much better.

### Questions
- Is there are description error in lines 045-048?  "two consecutive frames" ... "interpolate between these endpoints"  The methods section appears to indicate that this is about video interpolation strictly (If this is the case, it would be helpful to be more explicit in the introduction about the problem setting.), but the result section again talk about video prediction.  Which is it?  Could the paper improve the clarity of the problem setup?

- What does the notation $\mathcal{N}(a;b,c)$ mean?  The Normal distribution is specified by a mean and covariance; what is this additional term before the semicolon? This notation is used in (3) and (8).

- In eq.1, what are $z_x$ and $z_y$?  These are not defined.  In fact, the whole stage 2 description (176--183), is unclear.  What is the difference between a subscript and a superscript?  Is $z_x$ somehow $z^j$?

- Figure 1 seems misleading.  In this paper, a noise distribution is leveraged that is based on the "adjacent" frame, which is similar to how conditional diffusion works? Can the paper better differentiate the proposed method from conditional diffusion?

- What is the definition of $\theta$?

- Why is 3.2 called "Forward and Reverse Process"  There is only the Forward Process.

- Why are scalar $0,I$ sometimes used to specify the Normal, and sometimes bold?  Aren't they always vector/matrix elements?

- Are two context frames enough?  It seems from many of the qualitative visual results that the context frames may not adequately capture some of the rates of the motion in the scene.  Can the paper discuss this?

- How does the method guarantee the generation in latent space will be "coherent"?  It's plausible that a generated latent vector will be off the "manifold" of possible in-distribution images (given the high dimensionality),and hence decode to an unreasonable image frame.  How does the method protect against that?

### Soundness
2

### Presentation
1

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
The paper addresses latency constraints in diffusion-based video prediction, which arise from the need for multi-step sampling. This work proposes a method that represents videos as multi-dimensional continuous processes in latent space, allowing for reduced sampling steps and more efficient prediction of future video frames. Experiments are conducted on four benchmark video prediction datasets.

### Strengths
1) Motivation: The need to reduce latency in video generation is well-motivated and thoroughly explained.
2) Technical Soundness: The proposed model is concise and technically sound.
3) Clarity of Writing: The paper is well-written, making it easy to follow and understand.

### Weaknesses
The reviewer thinks the motivation of this paper is good, however, the contribution of this paper is incremental. 

Two main contributions are claimed in the paper,
1) Latent Video Representation: The paper proposes using a latent representation of videos/frames to reduce computational costs. However, leveraging latent visual representations to address computational efficiency is a recognized practice within the diffusion community. Prior work, such as PVDM [1] and Seer [2], has already demonstrated similar methods.
2) With the latent video representation, the second one is representing videos as multi-dimensional continuous processes. However, this seems to be a well-established framework used for this task. For example, the CVP [3], which is the previous SOTA compared in the paper, used this framework to generate the video futures.

### Questions
see the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2
