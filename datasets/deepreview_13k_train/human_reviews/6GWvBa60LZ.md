# A method for identifying causality in the response of nonlinear dynamical systems

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Predicting the response of nonlinear dynamical systems subject to random, broadband excitation is important across a range of scientific disciplines, such as structural dynamics and neuroscience. Building data-driven models requires experimental measurements of the system input and output, but it can be difficult to determine whether inaccuracies in the model stem from modelling errors or noise.  This paper presents a novel method to identify the causal component of the input-output data from measurements of a system in the presence of output noise, as a function of frequency, without needing a high fidelity model. An output prediction, calculated using an available model, is optimally combined with noisy measurements of the output to predict the input to the system. The parameters of the algorithm balance the two output signals and are utilised to calculate a nonlinear coherence metric as a measure of causality. This method is applicable to a broad class of nonlinear dynamical systems. There are currently no solutions to this problem in the absence of a complete benchmark model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a method for estimating the coherence $Co(y, y_n)$ between the observed noisy data $y_n$, and the “true” underlying system $y$. This estimate, termed $\hat{y}$ is obtained by combining, in frequency domain, a model/input based estimate $y_z$, with the noisy data $y_n$ (similar to a Kalman filter). The estimated $Co(y, y_n)$ is closer to $Co(y, y_n)$, than an only model/input-based estimate $Co(y_z, y_n)$.

### Strengths
- The method uses a sensible way to combine model/input based data with observed data.

- The resulting method outperforms the chosen baselines in terms of the coherence metric.

### Weaknesses
1. I found the paper hard to read, I think this can be improved by the authors more clearly explaining or motivating their motivation for the different steps (which might be obvious to them, but might not be to the reader), e.g.,  
    - 1.1 “Causality” is in the title and a key point of the paper, however I am totally missing some explicit motivation for why measuring coherence is the best way to estimate causality. The one citation for coherency (Silva et al., 2016), seems an odd choice.
    - 1.2 ANR introduced, but it, and the cited papers seem only tangentially related. This could be scrapped to make space for motivating the actual method, i.e., the use of coherency.
     - 1.3 No motivation is given for combining a model-based estimate with data in the frequency domain.
     - 1.4 Altough $\mathcal{F}$ of Eq. 1 is called a function, it is not a map from $x(t)$ to $y(t)$ (then there would be no dynamical system). Relatedly, it might also be better to use a different characters for $\mathcal{F}$ and $\mathcal{F}_\theta$, which are two very different things.

2. I find it very confusing that the paper introduces, and keeps referring to non-linear coherence, when the paper really seems to be after estimating the “standard”, linear coherence between $y$ and $y_n$.

3. Page 9, has half its space dedicated to a Figure of an experimental setup, but this is just another benchmark, I would suggest to make this Figure smaller (or move it to appendix), and use the remaining space to improve readability.

4. The only evaluation here is $Co(\hat{y},y)$, against other coherences, which is not immediately intuitive. Could the authors not simply also plot and/or quantify how close $\hat{y}$ is to $y$?

5. Fig. 1 seems to lack a $\hat{Y}$ before, and $\hat{y}$ after the IFFT box. $X$ and a box with $\mathcal{F}$ (with some parameters $\theta$?) feeding into $y_z$ would also be helpful.

6. I find the motivation for needing $\mathcal{L}y$ and $\lambda$ in general a bit lacking in theoretical foundations. A possible perspective could potentially be that Eq. 5 gives one the variational estimate of the true distribution of $y$ as $q(\hat{y}|y_n, x)$,  $F_\theta$ gives one $p(x|\hat{y})$ as $\mathcal{N}(x; F_\theta(\hat{y}), \sigma_x^2)$. If one adds a prior on $\hat{y}$ as p($\hat{y}$)=\mathcal{N}(y_n, \sigma_y^2)$ and writes out the typical ELBO loss on $p(x)$, both terms in Eq. 7 drop out (just the entropy of $q$ is missing) - although I am sure other perspectives are possible!

### Questions
1. Why is Wavenet a good baseline? If one wants to distinguish what combining the forward model with a data inferred state brings you, can one not simply take the forward model from section 3.3?
2. Are the $\dot{x}$ and $\ddot{x}$ terms in Eq. 3 needed (they seem to be absent in all benchmarks)?
3. Eq. 7, is there an implicit Gaussian assumption?
4. Line 197 Why would $\lambda=0$ yield the optimal $K$, this is not obvious to me?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The manuscript presents a novel technique for separate measurement noise and modeling errors without accessing the actual input-output relationship. The calculation was performed in frequency domain and there's one weighting parameter per frequency controlling the contribution of modeling error and measurement error to achieve minimum reconstruction error. The performance, measured by the coherence between actual signal and recovered signal is high.

### Strengths
- The presented method learns the a nonlinear functional mapping through a neural network. It works under a wide range of nonlinearities form as long as y can be mapped back to x (Eq.3).  
- It presented a novel way to balance modeling / observation error and contributed to maximize signal reconstruction performance in highly nonlinear systems. 
- Even in high noise cases, the recovered coherence was still high.

### Weaknesses
 - Only applies to the specific ODE described in Eq.3. Maybe the authors could extend it further as long as there's a one-to-one mapping from y to x? The current formulation seems limited to cases where the inverse mapping is straightforward and doesn't account for more complex nonlinearities that might introduce hysteresis or multi-valued mappings. It's unclear how the method would handle situations where the relationship between y and x is not strictly monotonic or where the inverse mapping is computationally expensive or unstable.
- the method only works from 1D signal to 1D signal? Is there any possibility to extend to high dimensional nonlinear systems. The current approach appears to be limited to single-input single-output systems. It's not clear how the method would generalize to multi-input multi-output (MIMO) systems where the nonlinearities may couple different dimensions. For instance, in a system with multiple interacting components, the method may not be able to separate noise and modeling errors effectively if the nonlinearities are not separable or if the measurement noise is correlated across different output channels.

### Questions
- What is the relationship between K and \lambda? Is K a hyper parameter during network training? How did you find the optimal K. 
- Why the modeling error / measurement error affects the signal in an additive way (Eq.4)

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
2

### Summary
The authors of the manuscript ‘A METHOD FOR IDENTIFYING CAUSALITY IN THE RESPONSE OF NONLINEAR DYNAMICAL SYSTEMS’ develop a method for the calculation of the nonlinear coherence between input and output data for a noisy ODE class given random input. The approach allows to learn an optimal combination of an output prediction with noisy measurements. The nonlinear coherence that is calculated is then used as a measure of causality. The method is shown to perform well on both simulated dynamical datasets as well as experimental data.

### Strengths
- The approach is well characterized mathematically in the manuscript.
- The demonstration of the approach over different types of simulated and experimental data is interesting.
- There are comparisons to alternative approaches over the same task.

### Weaknesses
 - The manuscript could be improved in terms of readability. It is in many cases very difficult to follow.
- While the method was evaluated over real experimental data, the noise was added synthetically.



### Questions
Comments:

- The description of the problem and approach in the abstract is not clear enough.
- Could you provide a more thorough statistical analysis of the performance of the approach for the simulated datasets over different parameter regimes of the underlying model, to show its robustness?
- The figures are missing captions.
- It would be informative, for the simulated and experimental results, to explicitly show how a better approximation of the response (as presented in the figures) helps in the interpretation of the original systems.

Minor comments:
- ‘but has recently begun’ - the ‘but’ part of the sentence should probably be rephrased
- it should be mentioned in the abstract that this work is restricted to a specific class of ODEs.
- ‘A completely new strategy’ - rephrase?
- The related work section sounds too defensive.. e.g. ‘The presented method .. is very different to work in the literature.’
- ‘In this paper, the primary aim is to estimate the noise level and the model error, but a similar principle is utilised.’ - unclear.
- ‘The presented method.. provides an excellent estimation of the nonlinear coherence for each noise case’ - rephrase in a more quantitative way?

### Soundness
2

### Presentation
1

### Contribution
2
