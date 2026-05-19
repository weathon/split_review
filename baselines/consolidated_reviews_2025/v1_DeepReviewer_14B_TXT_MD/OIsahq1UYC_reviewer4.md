### Summary

The paper proposes a new sampling method based on diffusion models. The main idea is to use the theory of generative flow networks (GFlowNets) to make use of intermediate learning signals. The method is evaluated on a number of benchmarks and compared to previously proposed methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and the method is well-motivated. The experimental results are promising and the method seems to outperform previously proposed methods on a number of benchmarks.

### Weaknesses

#### Some Related Works


#### comment

I have some concerns regarding the evaluation of the method. The authors only evaluate the method on a limited number of benchmarks and it is not clear how well the method would perform on other benchmarks. Additionally, the authors only compare the method to a few previously proposed methods and it is not clear how the method compares to other methods that have been proposed for sampling from intractable densities. Finally, the authors do not provide any theoretical guarantees for the method, which makes it difficult to assess the reliability of the method.

### Suggestions

The evaluation of the proposed method could be significantly strengthened by expanding the range of benchmarks used. While the current benchmarks provide some initial evidence of the method's performance, it is crucial to assess its robustness across a more diverse set of target distributions. Specifically, the authors should consider including benchmarks with varying levels of multimodality, dimensionality, and complexity. For instance, incorporating distributions with highly separated modes or those exhibiting strong correlations between variables would provide a more comprehensive evaluation of the method's ability to explore complex energy landscapes. Furthermore, it would be beneficial to include benchmarks that are commonly used in the literature for evaluating sampling algorithms, such as those found in the 'Benchmarking and Evaluation of Sampling Algorithms' paper, to allow for a more direct comparison with existing methods. This would help to establish the method's relative performance and identify its strengths and weaknesses in different scenarios.

In addition to expanding the benchmark suite, the authors should also provide a more thorough comparison with existing sampling methods. While the paper compares the proposed method to a few diffusion-based samplers, it would be beneficial to include comparisons with other classes of sampling algorithms, such as Hamiltonian Monte Carlo (HMC) and its variants, as well as other advanced MCMC techniques. This would provide a more complete picture of the method's performance relative to the state-of-the-art. Furthermore, the authors should consider comparing the method to normalizing flow-based samplers, which have shown promise in sampling from complex distributions. A detailed comparison should not only focus on the final sampling performance but also on the computational cost and convergence properties of each method. This would allow for a more informed assessment of the method's practical utility and its potential advantages over existing approaches.

Finally, the lack of theoretical guarantees for the proposed method is a significant limitation. While empirical results are important, a theoretical analysis of the method's convergence properties and error bounds would greatly enhance its credibility and reliability. Specifically, it would be valuable to investigate the conditions under which the method is guaranteed to converge to the target distribution and to derive bounds on the approximation error. This could involve analyzing the properties of the learned flow function and its relationship to the target distribution. Furthermore, it would be beneficial to explore the connection between the proposed method and existing theoretical frameworks for sampling, such as those based on Markov chain theory. Such theoretical insights would not only provide a deeper understanding of the method but also guide its further development and application.

### Questions

- How does the method perform on other benchmarks?
- How does the method compare to other methods that have been proposed for sampling from intractable densities?
- Are there any theoretical guarantees for the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
