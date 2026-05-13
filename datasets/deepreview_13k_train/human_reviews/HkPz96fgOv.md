# Energy-Efficient Sampling Using Stochastic Magnetic Tunnel Junctions

- Decision: Reject
- Scores: 5, 3, 8, 8

## Abstract
(Pseudo)random sampling, a costly yet widely used method in (probabilistic) machine learning and Markov Chain Monte Carlo algorithms, remains unfeasible on a truly large scale due to unmet computational requirements. We introduce an energy-efficient algorithm for uniform Float16 sampling, utilizing a room-temperature stochastic magnetic tunnel junction device to generate truly random floating-point numbers. By avoiding expensive symbolic computation and mapping physical phenomena directly to the statistical properties of the floating-point format and uniform distribution, our approach achieves a higher level of energy efficiency than the state-of-the-art Mersenne-Twister algorithm by a minimum factor of 9721 and an improvement factor of 5649 compared to the more energy-efficient PCG algorithm. Building on this sampling technique and hardware framework, we decompose arbitrary distributions into many non-overlapping approximative uniform distributions along with convolution and prior-likelihood operations, which allows us to sample from any 1D distribution without closed-form solutions. We provide measurements of the potential accumulated approximation errors, demonstrating the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents an energy-efficient algorithm for random sampling using stochastically switching magnetic tunnel junction (s-MTJ) devices. By directly mapping the physical properties of the s-MTJ to a uniform Float16 distribution, the proposed method avoids the computational overhead of symbolic calculations. Additionally, it introduces a method to sample from arbitrary 1D distributions using a mixture model approach, achieving low approximation errors.



Question:

### Strengths
1. The proposed framework is innovative, demonstrating both originality and significant potential in energy-efficient random sampling. The authors support these claims through simulations that indicate notable energy savings compared to existing methods.

2. By aligning the random generation process with the statistical properties of the Float16 format, this method sidesteps complex symbolic computations, enhancing both efficiency and simplicity.

3. By decomposing complex distributions into mixtures of uniform distributions, this approach allows for sampling from arbitrary 1D distributions without closed-form solutions, thus expanding the practical utility

### Weaknesses
1. The reliance on specific s-MTJ hardware may limit the method’s accessibility and applicability, particularly for researchers or practitioners who lack access to such specialized components, potentially requiring additional investment. The specialized nature of s-MTJ devices means that researchers without access to nanofabrication facilities or partnerships with institutions that do, will be unable to replicate or build upon this work. This dependence on specialized hardware creates a barrier to entry for many in the field.

2. Due to physical constraints in setting bias currents and control bits, there may be small approximation errors in generating the intended Bernoulli distributions, which could impact applications requiring precise random number distributions. It was also unclear if the ambient temperature of the chip would also impact the distributions (which is hard to control). The temperature sensitivity of s-MTJ devices is a significant concern, as variations in temperature can alter the switching probabilities and thus the generated distributions. This lack of precise control over the stochastic behavior could lead to inconsistencies and errors in applications that rely on accurate random number generation. Furthermore, the paper does not address the potential for device-to-device variability, which could further exacerbate the problem of achieving precise distributions.


### Questions
How does the presence of genuine randomness affect model stability and repeatability in long-running applications, especially in training deep models with dropout or other probabilistic methods?

Can you further clarify how the s-MJT would implement equations the operations on the sampled distributions (Eqns 11-16). Is the idea that these equations are done in some way off-line such that these operations amount to sampling?  I think this can be more clear. It would also be useful to understand if any other operation is typically necessary, such as a non-linear operation.

### Soundness
3

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
This paper presents a framework to generate uniform Floating-point numbers with stochastically switching magnetic tunnel junction (MTJ) devices. A collection of devices produces correctly sampled mantissa and exponent bits by tuning their Bernoulli distribution according to a closed-form solution. The authors compare their MTJ approach with the pseudo-random number algorithms Mersenne-Twister/PCG. Through SPICE simulation and measurements (Antunes & Hil 2024, Noureddine, 2022), an energy reduction of 9721x/5649x is shown. In addition, the authors explain the construction of general distribution from uniform ones and methods to sum and multiply them. They also present the analysis of the approximation errors.

### Strengths
A potential low-energy integrated framework for large-scale random number generation is shown. The methodology is straightforward and applicable to any source of tunable Bernoulli distributions. One of the applications includes probabilistic machine learning.

### Weaknesses
The paper presents a general framework for random number generation with MTJ or any Bernoulli source. Random number generation is part of many machine learning methods, but it is not clear how this is specifically relevant to an ML audience. The paper does not sufficiently articulate the unique advantages of this approach over existing methods in the context of machine learning. While the paper mentions probabilistic machine learning as an application, it lacks concrete examples of how this framework would improve specific ML algorithms or tasks. 

The paper presents the energy consumption resulting from the SPICE simulation of the devices and parts of the additional circuitry needed. Whereas for the reference measurements for the pseudo algorithms, there’s no indication of what kind of intermediate computations and memory operations are being done. In addition, the comparison is between the generation of Float16 and Int32 where it is not elaborated on how this affects energy consumption. Overall it is not clear how it is a fair comparison. The energy comparison is flawed because it does not account for the complete system-level energy consumption. The SPICE simulation only considers the energy of the MTJ devices and some peripheral circuits, but it neglects the energy required for data transfer, memory access, and other essential operations in a real-world implementation. Furthermore, the comparison between Float16 and Int32 generation is problematic because these formats have different bit lengths and computational complexities, making a direct energy comparison misleading. 

The methodology is only compared against pseudo-random generation algorithms, but not against other hardware solutions. Other previous work on generating random numbers with MTJs (Example of R. Zhang et al. https://doi.org/10.1002/advs.202402182) are not discussed. Thus, there is not sufficient coverage of existing work. The paper fails to adequately position its contribution within the broader landscape of hardware random number generation. The lack of comparison with other hardware-based RNGs, particularly those using MTJs, makes it difficult to assess the novelty and practical advantages of the proposed framework. The omission of relevant prior work, such as the example of R. Zhang et al., further weakens the paper's claims of originality and impact.

### Questions
- How does it compare to other relevant works on hardware random number generation?
- What parts of the framework are novel and not seen in other works?
- How much would the energy consumption increase if the devices were integrated into modern architecture? In other words, what other consumption of energy is required?
- How much is the energy consumption reduction for relevant ML applications?
- Would the integrated MTJ devices have a similar lifetime to current hardware?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors present a device capable of sampling one-dimensional distributions with arbitrary distributions, in float16 precisions. They describe how their device is more efficient at this task than standard hardware, and provide benchmarks which indicate orders of magnitude of energy efficiency gains through simulations of their hardware, both through cadence and through custom micromagnetic simulations.

### Strengths
The paper is well written, and the approach is clearly explained. 
The idea is scientifically sound, and the benchmarks are extensive and include very recent work (2024) that compares samplers. Two types of simulations were considered: i) through cadence, with the global foundries PDK, which includes realistic effects (though it is unclear what is/isn't included), and ii) through custom micromagnetic simulations, which are shown to match well theoretical predictions. I am not expert in these devices but it seems to me they have shown significant promise for a few years and this paper pushes the idea further and seems like a solid contribution to the field of sampling.

### Weaknesses
One weakness is that the device was only simulated and not actually realized, so uncertainty remains with respect to practical performance   (although the simulations are extensive, so I do not think this is a reason to reject).
I think the paper would benefit from a Limitations section, which would make it clear what effects were not captured in the simulations. For example, what about PVT variations?

Another weakness that may be improved on is the energy efficiency gain on downstream tasks, i.e., you show dramatic improvement over digital samplers, but how much impact would this have on a downstream task, say of a MCMC sampling task of a given probability distribution? This would be interesting to run with a software with pyro and show the overall energy efficiency improvement.

### Questions
Did you think about an extension to multidimensional probability distributions? I understand that this is a much more difficult problem, but it would be interesting to at least discuss it in the paper. Maybe some form of correlations may be implementable between s-MTJs which would allow for sampling of a given class of multidimensional probability distributions.

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
3

### Summary
The authors propose a hardware framework based on spintronic devices. By aggressively scaling the device down to nanoscale, thermal noise dominates the resistance state to enable randomness. In addition, the randomness can be biased by applying current through the device to accommodate arbitrary probability p in Bernoulli distribution. The authors use the above features to facilitate 16-bit floating point uniform sampling.

### Strengths
Sampling is essential in probabilistic models. The idea of using physical devices for efficient sampling is promising.

### Weaknesses
The devices do not seem to be readily deployable and may face manufacturing issues, thus may require further development.



### Questions
1. Sampling from a uniform distribution is the primary objective of this work and I greatly appreciate the authors' efforts in evaluating the error. Still, would it be possible to illustrate the actual distribution that the system is sampling from, given the limited number of control bits and the precision requirements indicated in Equation 6? So readers can have intuitive understandings. It would be great to show some zoom-in subfigures for detailed pdf variation in less-precise areas, too. 
2. For a 32-bit floating point, how would the actual distribution be like? How many control bits would it require to achieve sufficient sampling precision for 32-bit float? 
3. Since the probability of each bit can be atomically manipulated, is it feasible to use the system to sample an arbitrary distribution for arbitrary data format? I find this potential very intriguing.

### Soundness
2

### Presentation
3

### Contribution
3
