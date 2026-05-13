# BALSA: Benchmarking Active Learning Strategies for Autonomous laboratories

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Accelerating scientific discoveries holds significant potential to address some of the most pressing challenges facing society, from mitigating climate change to combating public health crises, such as the growing antibiotics resistance. The vast and complex nature of design parameter spaces makes identifying promising candidates both time-consuming and resource-intensive, rendering conventional exhaustive searches impractical. However, recent advancements in data-driven methods, particularly within the framework of "active learning," have led to more efficient strategies for scientific discovery. By iteratively identifying and labeling the most informative data points, these methods function in a closed loop, guiding experiments or simulations to accelerate the identification of optimal candidates while reducing the demand for data labeling. Despite these advancements, the lack of standardized benchmarks in this emerging field of autonomous scientific discovery impedes progress and limits its potential translational impact. To address this, we introduce BALSA: a comprehensive benchmark specifically designed for evaluating various search algorithms applied in autonomous laboratories within the active learning framework. BALSA offers a standardized evaluation protocol, provides a metric to characterize high-dimensional objective functions, and includes reference implementations of recent methodologies, with a focus on minimizing the data required to reach optimal results. It provides not only a suite of synthetic functions or controlled simulators but also real-world active learning tasks in biology and materials science — each presenting unique challenges for autonomous laboratory tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a benchmark suite for evaluating active learning strategies in autonomous laboratories. The work includes synthetic benchmark functions, two real-world tasks (protein design and electron microscopy), and introduces a new metric called landscape flatness to characterize objective functions. The authors evaluate 11 baseline methods on synthetic tasks and 4 methods on real-world applications.

### Strengths
* The authors provide a broad set of tasks, from synthetic to complex real-world scenarios in biology and materials science. The authors explain clear difference from traditional optimization benchmarks.
* The authors introduce the landscape flatness metric, which can quantify the complexity of the objective landscape.
* The authors provide detailed experiments with 11 baseline methods.

### Weaknesses
 * The authors do not provide enough validation for the proposed landscape flatness metric. It would be better to have theoretical evidence to support the robustness of this metric across different tasks. Specifically, the paper lacks a discussion on how the metric behaves under different conditions, such as varying levels of noise in the objective function or changes in the dimensionality of the search space. Without this, it's difficult to ascertain the reliability of the metric as a generalizable measure of landscape complexity.
* For experiments, the authors do not explain different numbers of trials (5 trials for synthetic tasks, 3 trials for real-world tasks). Results in Table 1 show high variance across trials, but the authors do not discuss this variation. The lack of justification for the different number of trials raises concerns about the statistical power of the results, especially for the real-world tasks with only 3 trials. The high variance observed in Table 1 further suggests that the conclusions drawn from these experiments might not be robust.
* The authors highlight the scalability as a key contribution, but the paper's analysis of this aspect is limited. For example, there is no quantitative analysis of how computation time scales with dimensionality. And the maximum dimension is 100D. The claim of scalability is not adequately supported by the experimental results. The absence of computational time analysis and the relatively low maximum dimensionality (100D) do not provide sufficient evidence to support the claim of scalability to high-dimensional problems.
* Others:
    * It is hard to understand the figures (e.g., Fig. 2, 6) due to small size, unclear labeling and limited context. The figures lack sufficient detail and clarity, making it difficult to interpret the results. The small size and unclear labeling hinder the reader's ability to understand the data being presented. 
    * The introduction contains redundant information about self-driving labs; Minor typo errors and inconsistencies are present in the paper.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
BALSA is a paper introducing new benchmarks for active learning in autonomous labs, both in the context of protein design and materials design. However, I get the feeling that the authors have tried to do too much, and I found the paper to be hard to read and poorly organized, though the ideas are certainly interesting. I think the paper could benefit from significant restructuring, and possibly even first perfecting the benchmark for protein design only, then extending to materials (or vice-versa); in its current state, it feels imperfect for both, and I did not feel that the paper adequately reviewed either existing protein design benchmarks or existing materials design benchmarks, making it hard to understand what is the value added here by BALSA. Datasets and benchmarks is perhaps the hardest track of papers in which to get accepted, as authors have to make things simple yet rigorous (i.e., foolproof) and transparent for other researchers to use, and I do not think BALSA in its current state meets this criteria.

### Strengths
* It is a good ambition to try and develop a suite of benchmarks that aim to ensure reproducibility of algorithmic performance across a wide variety of synthetic and real-world tasks.
* I like the idea of having the six functions as part of the benchmark (Ackley, Rastrigin, Rosenbrock, Griewank, Schwefel, and Michalewicz), but overall I think the benchmark in its current state does not seem general or rigorous enough to qualify for acceptance at ICLR.
* The plots themselves are very nice.

### Weaknesses
 * Unfortunately, the anonimized repository does not link to anything, which is a shame because it means the benchmarks introduced here are not reproducible.
* Not sure if AF2 is the most relevant model for evaluating the protein design tasks, as we are generally trying to push models outside distribution when designing new proteins, which is precisely the scenarios in which AF2 would fail. Furthermore, the materials benchmark proposed herein would only apply to crystalline materials, limiting its applicability. The choice of using electron ptychography data, while interesting, also restricts the scope of the benchmark to materials where this technique is applicable, which is not universal.
* It is not fully clear to me what is the novelty of the benchmarks introduced here, relative to previous benchmarks. The paper does not adequately discuss existing benchmarks in either protein or materials design, making it difficult to assess the value added by BALSA. A more thorough comparison to existing benchmarks is needed to justify the need for this new suite.
* The paper could benefit from a more thorough proofreading, including of the formatting which was strange in places throughout the text and distracting. For instance, the way references were inserted in the text made little sense to me and it as hard to understnad what part of the sentence was being referenced.

### Questions
* In active learning for molecular optimization (regardless of protein or materials), one of the most crucial components we seek to optimize is sample efficiency; however, it was not clear to me how this is assessed in this paper, even though the authors say this is what they are trying to assess. For instance, none of the presented results touch on sample efficiency (and, if they do, this was not clear). Can this be clarified?
* The figure and table captions are not informative, and could be improved for clarity. For instance, what are the values that are being shown in Table 1, is higher/lower better, and what are the bounds? Same for Table 2. What the values are could be made clear in the captions, without needing to go dig through the text (and, I could not always find what it was that was being shown in the tables).

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
5

### Summary
This paper aims to provide benchmark problems for active learning algorithms in automatically selecting experimental conditions in a Self-Driving Laboratory (laboratory automation). Laboratory automation is a field gaining attention across various disciplines, and establishing benchmarks for its core methodology, active learning methods, is essential. In this paper, benchmark problems using six artificial functions and two simulators are examined, and experiments are conducted on eleven types of active learning methods.

### Strengths
1. Laboratory automation is a field gaining attention and beginning to be explored across various disciplines; however, a lack of suitable benchmark problems makes it challenging to accurately assess the effectiveness of heuristic methods proposed from different fields. Efforts to establish benchmark problems for active learning in laboratory automation are, therefore, very important to address this issue.

2. The no-free lunch theorem implies that no single method excels universally across all optimization problems; methods should be chosen based on the specific type of problem. I fully support this author's view, as well as the approach of classifying and analyzing problem types according to the landscape smoothness of optimization problems.

### Weaknesses
1. I do not believe that the problem settings, datasets, and methods discussed in this paper are sufficient for evaluating algorithms for laboratory automation. First, it seems necessary to verify, in some way, whether benchmark functions such as Ackley and Rosenbrock sufficiently cover the class of optimization problems in laboratory automation. Since these benchmark functions were designed to measure the effectiveness of traditional nonlinear optimization algorithms, using them directly may not be appropriate. Specifically, these functions often assume a continuous search space, which may not accurately reflect the discrete or constrained nature of experimental parameters in laboratory settings. Furthermore, the landscape characteristics of these functions, such as their dimensionality and modality, may not align with the complexities encountered in real-world laboratory automation tasks, potentially leading to misleading performance evaluations of active learning algorithms.

2. Since this paper aims to provide benchmark problems, properly evaluating its originality for Top-tier conferences such as ICLR is difficult. However, for example, the metric presented as a novel measure for landscape flatness in Equation (2) is quite naive and not particularly new. A more original perspective tailored specifically to the issues in laboratory automation would strengthen this paper. The proposed metric appears to be a simple variance-based measure, which is a well-established concept in optimization and does not offer any novel insights into the specific challenges of laboratory automation landscapes. A more sophisticated metric, perhaps incorporating information about the local curvature or the presence of plateaus, would be more appropriate for characterizing the complexities of these landscapes.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
1
