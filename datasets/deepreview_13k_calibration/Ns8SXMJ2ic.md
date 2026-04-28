# Randomized Benchmarking of Local Zeroth-Order Optimizers for Variational Quantum Systems

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
In the field of quantum information, classical optimizers play an important role. From experimentalists optimizing their physical devices to theorists exploring variational quantum algorithms, many aspects of quantum information require the use of a classical optimizer. For this reason, there are many papers that benchmark the effectiveness of different optimizers for specific quantum optimization tasks and choices of parameterized algorithms. However, for researchers exploring new algorithms or physical devices, the insights from these studies don't necessarily translate. To address this concern, we compare the performance of classical optimizers across a series of partially-randomized tasks to more broadly sample the space of quantum optimization problems. We focus on local zeroth-order optimizers due to their generally favorable performance and query-efficiency on quantum systems. We discuss insights from these experiments that can help motivate future works to improve these optimizers for use on quantum systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper conducts a benchmark of local zeroth-order optimizers in the realm of quantum information, encompassing a range of partially randomized tasks. Through the comparative analysis of seven optimizers, the authors reveal a noteworthy trend: simpler heuristic methods, with SPSA at the forefront, frequently outperform their more intricate counterparts.

### Strengths
The submission conducts a systematic evaluation of local zeroth-order optimizers in quantum information, offering valuable insights that extend beyond specific quantum learning tasks. By conducting a comprehensive benchmark of seven optimizers across partially randomized scenarios, the authors provide practical guidance for using simpler heuristic methods like SPSA, to train variational quantum algorithms. Besides, the submission effectively communicates its motivation, ensuring clarity and comprehension for readers.

### Weaknesses
The submission appears to align with the benchmark paper category; however, it lacks key components that are typically expected in such a context. Benchmark papers typically aim to promote scalable, robust, and reproducible research. They often involve well-processed datasets, methods, and accessible results. Many benchmark papers also provide a dedicated website, offering documentation, example scripts, and a public leaderboard. Unfortunately, this submission falls short of meeting these essential criteria, as even the source code remains unreleased. Furthermore, the benchmark lacks a clear definition of the optimization problems being addressed. The partially randomized tasks are not sufficiently characterized, making it difficult to assess the generalizability of the results. The absence of a detailed description of the problem instances, such as the specific quantum circuits used or the parameter ranges explored, hinders the reproducibility of the study. Without this information, it is challenging for other researchers to replicate the experiments or extend the benchmark to new scenarios. The lack of a standardized evaluation protocol also makes it difficult to compare the results with other existing optimization methods in quantum information.

### Questions
The authors are encouraged to perform a comprehensive revision of their submission to ensure alignment with the formal benchmark paper format.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper benchmarks several SPSA-like (i.e., zeroth-order, local) optimizers on a randomized set of parametrized quantum learning problems (including Hamiltonian minimization and generative modeling). In each problem, the loss function is the expected value of a Hamiltonian. The authors focus on the noise-free setting and use the exact expected value in their experiments. Their findings are: (1) these optimizers are sensitive to hyperparameter tuning; (2) more elaborative optimizers are not generally better (the vanilla SPSA performs very well in most cases); (3) accelerated methods usually have a faster convergence rate.

### Strengths
Compared with prior arts, this work focuses on the performance of zeroth-order local minimizes across a series of partially randomized tasks in quantum learning. This methodology provides new insights into translating existing knowledge to new application scenarios. Details of the experiment setting are discussed and they look reasonable to me. The experiment results are illustrated in two ways: (1) convergence/loss plots and (2) box plots showing the statistics of the end-results. Overall, the manuscript is organized and well-written. The technical claims and numerical findings are plausible.

### Weaknesses
I feel this work is way too empirical with limited theoretical insights. In Section 5, some numerical findings are interesting (even counter-intuitive). It would be better to motivate and explain a bit more in terms of optimization theory. For example, in the 1D Ising & 2D Heisenberg experiments (and also the two generative models), adamSPSA has a much slower convergence than the vanilla SPSA. This is a bit surprising because ADAM often has faster convergence compared to the vanilla gradient descent. Is this because of the noisy gradient estimation (SPSA uses a zeroth-order oracle to estimate gradient), or a unique behavior only for quantum Hamiltonian minimization problems?

I also find that the 95% confidence interval in Figures 1 & 3 looks very thin. This is also a bit surprising because the optimization landscape for these problems should be highly nonconvex, and SPSA is a stochastic optimization algorithm. One explanation I could imagine is that the initial guesses are chosen in a small neighborhood in the parameter space so the loss curves have significant overlap. Or because the hyperparameter tuning only involves 3 random keys? Can you elaborate a bit more on this? Does this numerical methodology reflect the general landscape of quantum learning?

This work only studies the noiseless setting, while I feel the noisy setting is more relevant. Due to the Heisenberg limit, the expected value of the Hamiltonian can not be computed very accurately on a real quantum computer, unless the number of samples is large. On the other hand, SPSA is a zeroth-order optimization algorithm that is sensitive to random fluctuations in the function value. It would be more relevant to consider a benchmark with a reasonable noise model (or at least, an imperfect loss evaluation).

### Questions
A few questions can be found in the "Weakness" section. I suggest the authors add some discussions (or experiments) regarding the noise setting. Some previous results suggest that SPSA-like optimizers are still robust in the presence of noise. How are these results connected with the current work? Also, it would be appreciated for the authors to interpret their numerical results in the context of the landscape of these quantum learning problems. In practice, the knowledge of the target learning problem usually sheds light on what optimizers we want to choose.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on benchmarking local zeroth-order optimizers for variational quantum algorithms. The motivation behind this paper is to provide benchmarks and insights for understanding the performance of different optimizers in variational quantum learning problems. In addition to random parameter initialization, the authors also randomize the parameterized circuit/ansatz and objective to create a more diverse and realistic benchmark. By conducting experiments based on randomized tasks, the study provides findings and insights into the behavior of various optimizers.

### Strengths
The paper investigates an important issue in quantum machine learning, exploring the performance of classical optimizers for variational quantum systems. It has done a number of numerical experiments to present the findings and observations.

### Weaknesses
 - Lacks theoretical analysis and solid results to support the performance claims made for different optimizers.
- The experiments conducted in this study are limited in scope and scale. The small scale of the experiments (few qubits) limits the generalizability of the results and makes it challenging to draw robust conclusions. Specifically, the number of qubits used is not clearly stated for each experiment, and the maximum number of qubits explored is too low to be relevant for practical quantum machine learning applications. The absence of experiments with more than a handful of qubits makes it difficult to assess the scalability of the optimizers.
- Lacks clarity in presentation. It is not easy to follow and understand the experimental setups (e.g., algorithm, number of qubits, which kind of simulation). For instance, the specific quantum circuits used, beyond the general description of 'RandomLayers', are not detailed enough to allow for reproducibility. The simulation method (e.g., statevector, density matrix) is also not specified, which is crucial for understanding the computational cost and limitations of the experiments.
- The tasks considered in this paper are not general enough. The paper does not justify why the chosen tasks are representative of real-world quantum machine learning problems. The variety of tasks is also limited, which hinders the ability to draw general conclusions about the performance of the optimizers.
- Does not provide significant conceptual or technical contributions to quantum machine learning.

### Questions
- Considering the barren plateaus issue in many variational quantum algorithms, do the main results in this paper still hold? 
- What is the theory to guarantee that the randomized quantum circuit is random?
- What are the parameterized circuits used in this paper?
- What is the scalable analysis for the problem that the paper focuses on?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper benchmarks a variety of SPSA (and SPSA-esque) optimization algorithms on a suite of noiseless quantum machine learning tasks. The authors find that vanilla SPSA can work very well, although hyperparamter tuning is important (for SPSA as well as all optimizers).

### Strengths
- QML papers often go about selecting optimizers blindly, and it is always important to have a more rigorous and empirically informed approach to the problem
- The paper is generally well written and understandable

### Weaknesses
 - Two sentences start with “beyond” in the second paragraph (a minor point on readability)
- Figure 1 should have the exact solutions as a horizontal line. This makes it easier to understand the scale of the error.
- There are a few citations that this would benefit from using [1-3], some of which include randomised hamiltonians as a benchmark. 
- The core of my issue with this paper is that it doesn’t do enough to build on previous work. The results are not new, SPSA as a good non-parameter shift gradient optimizer and the importance of hyperparameter tuning are both mentioned in [2]. Although more verification and more problem evaluation is always good, the results and methods are generally similar to a growing lineage of QML optimization benchmarks. 
- SPSA would benefit from more mathematical background and explanation when first presented.
- This paper does not seem geared towards (a decent knowledge of QML is necessary for appreciation of the paper, and it does not make much of an attempt to familiarize people with it. This is not a slight against the paper a priori, just a specific concern with this venue), nor necessarily of great interest to, the ICLR community (which is largely dominated by classical ML researchers). 
- Given the known dependence of optimization difficulty of QML systems on circuit width and depth (even for non gradient based optimizers [4]), this paper would benefit from more consideration and analysis of these (since the size and widths seem picked somewhat arbitrarily). 

### Questions
- Would the code be available if the publication is accepted?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
