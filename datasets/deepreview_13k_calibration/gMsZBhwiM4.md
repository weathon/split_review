# ICA model estimation using an optimized version of genetic algorithms

- Decision: Reject
- Avg Score: 3.33
- Scores: 1, 3, 6

## Abstract
This paper presents a method of estimating the independent component analysis model based on the use of a training algorithm based on an optimized version of genetic algorithms with a neural network algorithm. The mixed training algorithm is applied to optimize the objective function negentropy used to estimate the ICA model. The proposed estimation algorithm improves the training scheme based on genetic algorithms by using for crossover the most suitable chromosomes evaluated by the objective function with the parameters calculated calculated accordingly by a multilayer neural network algorithm. The performances of the proposed algorithm for estimating the independent components were evaluated through a comparative analysis with the versions of FastICA algorithms based on the standard Newton method, as well as on the secant method of derivation of the training scheme at the level of the optimization stage of the approximate objective function. The experimental results for the proposed algorithm for estimating the independent components are established in specific blind source separation applications using unidimensional and bidimensional signals.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper uses a genetic algorithm to achieve ICA. Formally, the search space is that of vectors $w$ on the sphere ($\|w\| = 1$) of dimension $d$, where the dimension of the data is $d$. The objective function is that of the fast ICA method.

### Strengths
We are prepared to believe that GAs and stochastic optimization at large might advance the state of the art in problems that are not amenable to mainstream optimization. This paper asks the excellent question of whether GAs can be used to advance the state of the art in Fast ICA,

### Weaknesses
 - While FastICA is a well-known ICA method, there exist a lot of improved algorithms for ICA. The proposed method should be compared to state-of-the-art ICA algorithms and FastICA variants to demonstrate its effectiveness.
- The existing works already attempt to use a genetic algorithm for ICA. For example, 
    * G. Wen, C. Zhang, Z. Lin, Z. Shang, H. Wang and Q. Zhang, "Independent component analysis based on genetic algorithms," 2014 10th International Conference on Natural Computation (ICNC), Xiamen, China, 2014, pp. 214-218, doi: 10.1109/ICNC.2014.6975837.
    * H. Azad and M. Hatam, "Maximum likelihood independent component analysis using GA and PSO," 2016 24th Iranian Conference on Electrical Engineering (ICEE), Shiraz, Iran, 2016, pp. 776-781, doi: 10.1109/IranianCEE.2016.7585625.
- The justification and design principle of the proposed method is unclear. In addition, the reason for the performance improvement by the proposed method is also unclear.
- There are many typos and unclear descriptions in the paper.

### Questions
Complementary experiments are required to assess the proposed approach and its scalability w.r.t. the dimension of the problem. 
The comparison with recent baselines is mandatory.

See for instance the experimental setting in: Stochastic algorithms with descent guarantees for ICA, 2019.
Older: Consistent sparse representations of EEG ERP and ICA components based on wavelet and chirplet dictionaries, 2010.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a genetic algorithm and neural network-based optimization method for independent component analysis. The loss function used in the proposed method is the same one in the FastICA algorithm. The performance of the proposed method is experimentally compared to the FastICA variants on artificial and face image datasets.

### Strengths
- A new genetic algorithm-based optimization method for ICA is presented.

### Weaknesses
- While FastICA is a well-known ICA method, there exist a lot of improved algorithms for ICA. The proposed method should be compared to state-of-the-art ICA algorithms and FastICA variants to demonstrate its effectiveness.
- The existing works already attempt to use a genetic algorithm for ICA. For example, 
    * G. Wen, C. Zhang, Z. Lin, Z. Shang, H. Wang and Q. Zhang, "Independent component analysis based on genetic algorithms," 2014 10th International Conference on Natural Computation (ICNC), Xiamen, China, 2014, pp. 214-218, doi: 10.1109/ICNC.2014.6975837.
    * H. Azad and M. Hatam, "Maximum likelihood independent component analysis using GA and PSO," 2016 24th Iranian Conference on Electrical Engineering (ICEE), Shiraz, Iran, 2016, pp. 776-781, doi: 10.1109/IranianCEE.2016.7585625.
- The justification and design principle of the proposed method is unclear. In addition, the reason for the performance improvement by the proposed method is also unclear.
- There are many typos and unclear descriptions in the paper.

### Questions
- How is the computational cost of the proposed method for ICA optimization compared to other ICA algorithms?
- I cannot identify the role of the neural network in the proposed method. It would be better to clarify the detailed algorithm, including the input/output and training data of the neural network, and the advantages of using the neural network.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a mixed algorithm based on a genetic algorithm and neural network for ICA model estimation. After the algorithm descriptions, some experiments are provided for verification.

### Strengths
Using other algorithms for the ICA model estimation may be a new research direction

### Weaknesses
I am not familiar with ICA, so I cannot exactly evaluate how much the contribution of the proposed work in this paper to the community of ICA. However, in my personal view, there is much new thing in using genetic algorithms with neural networks for optimization tasks. Compared to the traditional methods, the used methods are often not effective, and the results are also not always with the same values. Unfortunately, I did not see such kinds of discussion.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
