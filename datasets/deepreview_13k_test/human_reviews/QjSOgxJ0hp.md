# Learning from End User Data with Shuffled Differential Privacy

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
We study a setting of collecting and learning from private data distributed across end users.
In the shuffled model of differential privacy, the end users partially protect their data locally before sharing it, and their data is also anonymized during its collection to enhance privacy. 
This model has recently become a prominent alternative to central DP, which requires full trust in a central data curator, and local DP, where fully local data protection takes a steep toll on downstream accuracy. 

Our main technical result is a shuffled DP protocol for privately estimating the kernel density function of a distributed dataset, with accuracy essentially matching central DP. 
We use it to privately learn a classifier from the end user data, by learning a private density function per class. 
Moreover, we show that the density function itself can recover the semantic content of its class, despite having been learned in the absence of any unprotected data. 
Our experiments show the favorable downstream performance of our approach, and highlight key downstream considerations and trade-offs in a practical ML deployment of shuffled DP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies kernel density estimation (KDE) under shuffle DP, which is suitable for the setting where users do not persistently participate in training. The authors prove convergence for Gaussian kernel and test their algorithm on various datasets.

### Strengths
1. Kernel density estimation is an important machine learning problem, and shuffle DP is an important intermediate privacy model between local and central DP.
2. The authors conducted extensive experiments on various datasets.

### Weaknesses
1. The algorithm proposed in this work mainly seems like an application of bitsum algorithm. The authors should highlight the novelty in either the algorithm design or theoretical analysis. For example, what is the main difficulty in applying to kernel density estimation
2. The algorithm does not demonstrate a consistent good performance. The performance is bad for inner product kernel and shuffle-DP algorithms other than 3NB (Bhadi et.al. 2020).
3. The authors claimed that there is no need to optimize the bandwidth for the Gaussian kernel. However, by shrinking the dataset by some factor, one can equivalently view this as changing the bandwidth. Thus, this claim may not be justified.

======= Update =======
Increased my score to 6 after the author's response.

### Questions
How can the algorithm adapt to new users joining in and we need to update the kernel density?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method to perform kernel density estimation (KDE) under Shuffle model of differential privacy (Shuffle-DP).

The KDE problem is as follows: Given datapoints $X = (x_1, \ldots, x_n)$ and a query point $y$ (all points in $\mathbb{R}^d$), the goal is to compute $\mathrm{KDE}\_X(y) := \frac1n \sum\_{i=1}^n \mathbf{k}(x\_i, y)$ for a given kernel $\mathbf{k}$.

The Shuffle-DP is the setting where messages from the users are sent to a shuffler that randomly permutes all received messages before sending it to the analyst, and it is required that the multi-set of messages received by the analyst satisfies differential privacy.
Various Shuffle-DP mechanisms are known in literature for computing "Bit-sums", wherein, each user holds a single bit $x_i \in \{0, 1\}$ and the goal is to estimate their sum $\sum_i x_i$.

The main technique in this paper is to reduce the problem of KDE to Bit-sums, for kernels $\mathbf{k}$ that admit "(approximate) locality sensitive quantization (LSQ)". This means that there is a distribution $\mathcal{Q}$ over pairs of functions $(f, g)$ each mapping $\mathbb{R}^d \to [-R, R]^Q$ such that $\mathbb{E}_{(f, g) \sim \mathcal{Q}} [f(x)^T g(y)]$ is equal to (or closely approximates) $\mathbf{k}(x, y)$ for all $x, y \in \mathbb{R}^d$.

Thus, given access to $f_i(x_j)$ for $i \in \{1, \ldots, I\}$ and all $x_j \in X$, one can approximate $\mathbf{k}(x, y)$ as $\frac1I \sum\_{i=1}^I \sum\_{x \in X} f\_i(x)^T g\_i(y)$.

Finally, the $f_i(x_j)$ themselves are estimated by reducing to "Bit-sums" through randomized rounding.

Finally it is standard to use KDE for solving classification tasks, by performing a KDE on examples of each class, and on given query point $y$, return the class with the largest kernel density estimate.

The paper provides bounds on the communication cost and root-mean-squared-error (worst case over all query points $y$).

The paper also provides experimental evaluation on three textual datasets (two on topic classification, one on sentiment classification) and an image classification dataset (CIFAR-10), and evaluates the performance of two kernels (Gaussian kernel and Inner Product kernel) in three regimes: (i) without privacy, (ii) central DP and (iii) shuffled DP.

### Strengths
The paper proposes a novel application of Bit-sums in Shuffle-DP to the problem of Kernel Density Estimation. The idea is simple and easy to implement. The paper has rigorous theoretical bounds on the error.

Overall the paper is well written and easy to read.

### Weaknesses
This is not particularly a "weakness", but the approach in the paper is limited to kernels that admit good locality sensitive quantization.

### Questions
I would imagine that the theoretical bounds on the $\mathrm{supRMSE}$ in Theorem 3.2 are quite loose. Would it be possible to add a comparison of the theoretical bounds alongside the empirically realized errors in KDE ?

For example, I am surprised that for the IP kernel, it is better to go with the $(1, \sqrt{d}, 1)$-LSQ instead of the naive $(d, 1, d)$-LSQ. While the latter has additional dimension, it is no variance, whereas the former has a large variance, even if it is $1$ dimensional. But I don't see the bounds in Theorem 3.2 accounting for the variance in the LSQ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on learning a kernel density estimator (KDE) under shuffled differential privacy (SDP), while the learned KDEs are used for a downstream classification task. The proposed method first estimates noisy class counts under local DP, and then learns KDE for each class using the noisy counts (and the corresponding class assignments) for calibrating SDP noise level. The method for estimating KDE is based on the notion of locality-sensitive quantization (LSQ), which also allows the authors to prove general as well as more specific utility bounds (e.g. for Gaussian kernel with random Fourier features). The authors experimentally demonstrate their proposed method on several data sets using various existing SDP summation protocols together with Gaussian and inner product kernels.

### Strengths
i) The proposed method seems to be interesting and novel in the SDP setting.

ii) The paper is mostly well-written and nice to read, with no obvious major oversights.

iii) The code is included with the submission (at least partly; e.g., as there is no requirements.txt or equivalent, getting the code to run would take some amount of effort).

### Weaknesses
i) While the stated goal is to do learning in a "single-shot" manner, i.e., without clients participating (iteratively) in training beyond just choosing to send their data, the proposed approach still involves 2 communication rounds (getting noisy counts for the classes, then running the KDE protocol with noisy class sizes) and a non-trivial amount of compute spend on client-side (run some pretrained model as feature-extractor, run Alg.1 with given hypers).

ii) See comments below for some additional specific concerns.

### Questions
## Update after the discussion:

The authors have mostly responded well to all my expressed concerns; I still have some minor disagreements, e.g., over the class decoding, but these are minor points and should not prevent accepting the paper. I have increased my score accordingly.

## Original questions:

In decreasing order of importance:

1) On the distinction between classification and class decoding, e.g. lines 315-27, 526-29: I am not sure how meaningful this difference actually is; I would expect that to be able to classify examples well, the KDE $\tilde K_c$ for any given class $c \in [m]$  should give higher scores than any other KDE for that class. This seems pretty much the same things as any given KDE $\tilde K_c$ being able to give high scores for inputs from the matching class $c$ and lower scores to inputs from any other class. Whether or not this matches what humans would consider to be semantically relevant for the classes seems like quite a fuzzy claim.

2) Experimental details: please specify how all hyperparameters have been set, how many seeds you used etc. Also, please add some error metrics (sem, std or similar) to the results.

3) How much utility do the noisy counts via LDP cost? Please add an ablation study (at least for some experimental setting) using the actual true counts and comparing to the proposed full method with LDP counts (using same noise levels for the shuffle protocol).

4) Thms 3.2, 3.3: please clarify in what sense the bit-width 1 is optimal (e.g. communication, utility, both)?

5) Lines 312-14: there are some proposed DP-kNN methods, so this claim does not seem to be true (although I haven not read the said papers in detail).

6) Please add an additional step after line 913 to be clearer on the proof.

## Minor typos, comments etc. 

I do not expect any acknowledgement or comment on these, just fix when appropriate:
* typos: lines 109-110, 775-76, 1063-64, 1139-40, 1160-61
* Why suppress eq numbers? Would be more straightforward to ref these using numbers instead of lines.
* To make the result figures more readily interpretable, it would be good to add some more basic info to the captions (e.g. $\delta$, how many repeats).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies private kernel density estimation and the privacy at the user end is considered. The methodology is with the protocol of the shuffled-DP: each user first randomize her own data and then a shuffler will collect the randomized messages from all users and shuffle them in a random order. The basic module is the bitsum in the shuffled DP where each user has one bit and the set of bit after shuffling keeps well the sum of all bits. The main algorithm is designed to call this module towards the private kernel estimation. The paper provides the theoretical guarantee for the algorithm. In the experiment, the proposed algorithm under shuffled-DP is compared with the algorithm at central-DP in two downstream tasks classification and class decoding.

### Strengths
1. The flow of the writing and the clarity are great. The background such as the framework of shuffled DP is mostly well-introduced; I do have questions for some concepts (see the question section), but they are not influencing my overall understanding for the method.
2. The analysis of proposed algorithm seems solid as presented in theorem 3.2 and theorem 3.3.
3. The empirical evaluation is systematic. It is located to two downstream tasks of the private kernel estimation.

### Weaknesses
As this paper is the first paper (to my best knowledge) to study private kernel estimation with the shuffled DP protocol, I think more comparison with other settings can enhance the understanding what role shuffled DP plays. In details:
1. How is the proposed method compared with central DP in terms of theoretical guarantees? Would this be aligned with the empirical comparison as shown in the experiment section?
2. Another popular framework is to leverage secure multiparty computation (MPC) to compute sums of values from each user [1]. What is the advantage and limitations between these two framework in terms of utility and communication cost?

[1] Bonawitz, Keith, et al. "Practical secure aggregation for privacy-preserving machine learning." proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. 2017.

### Questions
Please see the weaknesses section. Moreover, I have some questions of some mentioned concepts:
1. Bit-width is introduced in line 239-240. What is the exact definition of it? In the theorem, "the protocol has optimal bit-width 1" is stated; what does this mean?
2. $S$ is introduced in Definition 2 as a property to describe the kernel. It does not appear in the algorithm's description but seems to be an important factor for the theoretical guarantees, which occurs in both DP's guarantee and the utility upper bound. Could you explain what role $S$ plays to bring these effects on the theoretical results?

### Soundness
3

### Presentation
3

### Contribution
2
