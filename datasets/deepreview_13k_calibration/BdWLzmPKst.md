# Sequential Data Generation with Groupwise Diffusion Process

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
We present the Groupwise Diffusion Model (GDM), which divides data into multiple groups and diffuses one group at one time interval in the forward diffusion process. GDM generates data sequentially from one group at one time interval, leading to several interesting properties. First, as an extension of diffusion models, GDM generalizes certain forms of autoregressive models and cascaded diffusion models. As a unified framework, GDM allows us to investigate design choices that have been overlooked in previous works, such as data-grouping strategy and order of generation. Furthermore, since one group of the initial noise affects only a certain group of the generated data, latent space now possesses group-wise interpretable meaning. We can further extend GDM to the frequency domain where the forward process sequentially diffuses each group of frequency components. Dividing the frequency bands of the data as groups allows the latent variables to become a hierarchical representation where individual groups encode data at different levels of abstraction. We demonstrate several applications of such representation including disentanglement of semantic attributes, image editing, and generating variations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on groupwise diffusion process, namely GPM. The key is that it generates one sample at a time for each group. This new framework generalizes to the autoregressive model in certain circumstances. Another benefit is that the latent space becomes interpretable because of the group-wise generative process. The GPM further extends to the frequency domain, allowing each group to encode data at different frequency levels. The authors demontrate several applications like image editing, disentangled image semantic attributes, and generating variations.

### Strengths
- The GPM proposed in the papers is quite interesting along with its properties. It can be extended to the frequency domain. 
- The demonstrated examples are promising.
- It adds new connections between GDM and certain forms of autoregressive models and cascaded diffusion models.

### Weaknesses
 - It seems that the number of groups, k, is a hyperparameter where not much discussion is given.
- There are no comparisons to other generative models like VAE or GAN or even guided diffusion.

### Questions
1. How do you choose the number of groups?
2. If we set the number of groups equal to 1, what should we expect? How does it compare with the generated data from DDPM or DDIM?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose GDM that generalizes the diffusion process by grouping the data into different blocks and applying different schedule to each block. Specifically, it shows that an Bottom→Top scheme to partite the data is able to improve the general generating performance.

### Strengths
The groupwise diffusion model is a unified model of some existing works. And the authors take effort to combine this model with other approaches such as frequency domain as well as conducting a lot of experiment to demonstrate the approach.

### Weaknesses
1. Overall, I find this method has limited novelty. It is a simple extension of the model such as rectified flow by using a matrix interpolation function. The specific form of the interpolation, while perhaps not previously explored in this exact manner, does not fundamentally alter the underlying diffusion process. The core idea of applying different schedules to different parts of the data is conceptually straightforward, and the use of a matrix interpolation function, while technically sound, feels like a minor variation rather than a significant innovation. The connection to autoregressive models, while interesting, does not elevate the method to a level of substantial novelty given the relatively simple interpolation function used.

2. When applied to the real problem, this approach seems adhoc. It is not explained and supported that why we should partite the data by a certain order and why such partition gives better generation quality. The lack of a clear theoretical justification for the bottom-to-top approach, or any specific ordering, makes the method feel empirically driven without a strong underlying principle. The authors do not provide a mechanism to determine the optimal grouping and ordering for a given dataset, which limits the practical applicability of the method. The experimental results, while demonstrating some performance gains, do not offer sufficient insight into the underlying reasons for these gains, making the approach feel somewhat arbitrary.

### Questions
Can you explain why partite the data by a bottom->top approach is better than others?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a Groupwise Diffusion Model (GDM), which uses a new type of forward process, for the interpolation between data $\boldsymbol{x}$ and noise $\boldsymbol{z}$ by dividing data into multiple groups and diffusing one group at once. The authors provide an extension to the frequency domain termed as GDM-F. The work claims that a notable characteristic of GDM is that the latent space now possesses group-wise interpretable meaning, for instance to attribute changes in features of an image.

### Strengths
Originality: To the best of my knowledge the work seems original, based on the groupwise strategy as an alternative forward process in diffusion models.  

Quality: The experiments presented in the work look convincing.

Clarity: The work does not properly explain the methodology of the groupwise strategy which it is the key point in the work. There are some problems in the mathematical notations and inconsistencies.

Significance (importance): The work presents interesting experiments that might be quite useful for the practitioners in the field. There is an interesting contribution regarding a more controlled interpretability when using diffusion models.

### Weaknesses
-The work lacks a clear connection between the proposed methodology and the experimental results, making it difficult for the reader to fully grasp the implications of the groupwise strategy. For example, the connection between manipulating a single element in the latent vector (as shown in Fig. 6) and the theoretical underpinnings of the method, including the specific equations, is not adequately established.

-The methodology, particularly the groupwise strategy, is not explained with sufficient clarity. There are inconsistencies and ambiguities in the mathematical notations. For instance, the variable \(\boldsymbol{x_{\theta}}\) is not introduced before its appearance in Eq. (3), and the meaning of \(\boldsymbol{\theta}\) in the minimization argument is unclear. The double notation for \(\boldsymbol{v_{\theta}}\) or \(\mathbf{v_{\theta}}\) further adds to the confusion. The explanation of data division in Section 3.1 is vague, particularly regarding the definition and meaning of each \(S_i\) in the partition \(\{S j \}^k_{j=1}\).

-The presentation of results is problematic. Figures are cited out of order and do not appear in a logical sequence, disrupting the flow of the paper. For instance, Fig. 5 and Fig. 4 are mentioned in a way that does not align with their order of appearance.

### Questions
---Specific comments---

-Shouldn't the title be "Sequential Data Generation with Group-wise Diffusion Processes" or "Sequential Data Generation with a Group-wise Diffusion Process"? 

-After Eq. (1): It appears a variable "$a$" instead of "$\alpha$", $a(0)=1$ and $a(1)\approx 0	$, is it a typo? Or what is $a$?

-Before Eq. (2): correct singular or plural in "some recent work instead use the linear interpolation", "...recent work uses the linear" or "...recent works use"?

-In Eq. (3): the variable $\boldsymbol{x_{\theta}}$ was not introduced. Also, what is $\boldsymbol{\theta}$ in the minimization argument? It was not introduced.

-Before Eq. (4): There is a double notation for the variable $\boldsymbol{v_{\theta}}$ or $\mathbf{v_{\theta}}$, or are they different?

-Include a comma "," after Eq. (2) and Eq. (3).

-Section 3.1: I believe the first paragraph should be rewritten in a more detailed way. This paragraph is key to lead the reader to understand the way data division in performed. For instance, it is not clear "we divide
data into $1 \leq k \leq d$ groups", does this mean we divide the data into any possible integer in the interval $1 \leq k \leq d$, then that integer value represents the number of groups? Or is it that you want to divide data into a number of $d$ groups, where each group has a length of $k$? Shouldn't we refer to the total number of data and then refer to the splits of that number as per your method proposes? 

-Also Section 3.1: It suddenly appears "we divide the indices $\{1, ..., d\}$ into a partition $\{S j \}^k_{j=1}$". Do you divide the set $\{1, ..., d\}$ into another set $\{S_1,S_2...,S_k\}$? So, what is the meaning or definition of each $S_i$?
That is not clear to me.

-At the end of Section 3.1: It reads "the elements of j-th latent group are diffused into noise", what is a latent group? When was the name latent group introduced? Or what variable corresponds to such a latent group?

-Before Eq. (8): It reads "Instead, we find that it is beneficial to define $\mathbf{u_{\theta}}$", why is it beneficial? It is important to include the explanation in the phrase to guide the reader.

-There is no consistence with the figures when they are cited in the text and when they appear. See for instance Fig. 5 and Fig. 4.

-In the experiments section: It might be quite important to be able to interconnect what it was derived in the methodology with the experiments. For instance where it reads "Fig. 6 shows that manipulating a single element in the latent vector of the lowest
frequency band results in a change in a single high-level attribute of images.", where is that latent vector appearing in the methodology, what Equation? how can the reader understand from the methodology where the variable that seems quite important is appearing. What is the dimensionality of such a variable?

-Introduce the acronym FID!

-Include comma "," after Eq. (2) and (3).

-Period "." after Eq. (8).

---Other Questions---

-In the Fig. 6 where traversing a single latent variable is associated to a particular featured changed in the images, what is the effect of traversing other elements like (2), (3), (10) or (20)?

-In the practice, in which scenarios should we apply GDM or GDM-F?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good
