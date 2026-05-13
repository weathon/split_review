# Geometry-Informed Neural Networks

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Geometry is a ubiquitous tool in computer graphics, design, and engineering.
However, the lack of large shape datasets limits the application of state-of-the-art supervised learning methods and motivates the exploration of alternative learning strategies. 
To this end, we introduce geometry-informed neural networks (GINNs) -- a framework for training shape-generative neural fields \emph{without data} by leveraging user-specified design requirements in the form of objectives and constraints.
By adding \emph{diversity} as an explicit constraint, GINNs avoid mode-collapse and can generate multiple diverse solutions, often required in geometry tasks.
Experimentally, we apply GINNs to several validation problems and a realistic 3D engineering design problem, showing control over geometrical and topological properties, such as surface smoothness or the number of holes.
These results demonstrate the potential of training shape-generative models without data, paving the way for new generative design approaches without large datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a novel framework for data-free geometry learning. The framework relies on implicit geometry representation - which is a  modulated conditional neural field - where conditioning is on latent variables to ensure diversity. Given such a representation, authors propose to formulate a constrained optimization problem, in practice written down as a set of differentiable losses. The proposed constraints include: minimizing genus, smoothness, and diversity of generated shapes. Authors conduct a series of toy experiments to validate the model, and test it on a single engineering design problem.

### Strengths
+ Paper is well-written and is easy to follow.
+ Overall framework is meaningful and has a large number of potential applications (in particular in generative design and shape optimization).
+ The promise of representation that does not require significant amount of data is very valuable specifically because the amount of data in generative design is often scarce or requires expensive simulations. 
+ Diversity measure that is demonstrated to work in practice for tackling mode collapse in implicit field learning is a potentially a critical contribution.

### Weaknesses
- (minor) Most of the proposed constraints have been developed in previous work. 
- (minor) For the method to actually be useful for the real-world applications (e.g. in shape optimization in engineering fields), a mapping to an explicit representation could be a hard requirement to be compatible with existing simulation.  The current implicit representation, while flexible, lacks direct compatibility with standard CAD/CAE workflows that rely on explicit boundary representations such as meshes or NURBS surfaces. This discrepancy poses a significant hurdle for practical adoption in engineering design. 
- Although the representation/optimization framework that does not require data has promise, it would be interesting to see if these methods can be used in combination with available data.  The current approach focuses solely on data-free learning, which might limit its performance in scenarios where even a small amount of data is available. Exploring how to effectively integrate data could lead to more robust and accurate results. 
- The experimental evaluation is very limited. In particular for shape optimization (which is the only truly realistic test iiuc), there is only single example provided, which makes it hard to understand how much of the results is due to parameter tuning. The lack of diversity in the test cases makes it difficult to assess the generalizability of the method. The single engineering design example, while promising, is insufficient to demonstrate the method's robustness and applicability across different design problems.

### Questions
- How robust is the method to the choice of hyperparameters?
- Would it be possible to demonstrate results on more than one example for engineering design?

### Soundness
2

### Presentation
3

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
This paper presents a framework for achieving controllable generation of industrial part geometry. Specifically, the authors utilize an implicit neural field to represent the surface of industrial parts. Through optimization objectives in different aspects, the implicit neural field is adjusted to closely match the given targets, such as ensuring the zero-level set of the implicit field aligns with the geometric surface and the first-order derivatives of the implicit field align with the surface normals. Additionally, the authors attempt to introduce a regularization term to promote diverse optimization results. Finally, the authors conduct experiments on a challenging example and demonstrate the effectiveness of their approach.

### Strengths
This paper presents a well-formulated approach for shape-generative modeling driven by geometric constraints and objectives. It starts by considering the problem from a theoretical perspective and successfully translates it into an executable framework. The research problem addressed in this paper is valuable, and the preliminary experimental results provided by the authors demonstrate the effectiveness of their proposed method. Additionally, the paper is well-written and easy to follow.

### Weaknesses
The framework solution proposed in the paper is effective from a high-level perspective, but I anticipate numerous challenges when it comes to practical implementation. My primary concern is whether we truly have the capability to account for all objective functions based on individual intuition, especially considering that these functions must be feasible, differentiable, and ideally, non-conflicting. For instance, how should we approach the generation of a nut that matches a specific type of screw, or a particular joint bearing? The challenge lies in defining the precise mathematical formulations for complex mating conditions and ensuring these formulations are compatible with the optimization process. This requires not only a deep understanding of the desired geometric constraints but also a careful consideration of how these constraints interact within the implicit neural field representation.

Moreover, while the article emphasizes its data-free approach, it appears to me as an optimization-based strategy, with the optimization target being the implicit field represented by the neural network—a relatively conventional method. I do not find this particularly innovative. The core of the method relies on iteratively adjusting the neural network's weights to minimize a loss function defined by the geometric constraints. This process is fundamentally an optimization problem, similar to many existing techniques that use neural networks for shape representation and manipulation. The novelty, therefore, is not in the optimization process itself, but rather in the specific formulation of the loss function and the use of an implicit neural field.

Additionally, although Figure 6 does showcase a variety of workpieces, I doubt the compliance of these pieces with standard usage requirements; many seem to be diverse merely for the sake of diversity. The generated shapes appear to prioritize surface smoothness and geometric variation over functional requirements. This raises concerns about the practical applicability of the method for generating parts that meet real-world engineering standards. Lastly, the experiments are conducted on only one workpiece, which, despite its complexity, does not suffice to demonstrate the universality of the method. While the jet engine bracket is a complex example, it is still a single instance and does not provide sufficient evidence that the method can be generalized to other types of industrial parts with different geometric and functional requirements.

### Questions
Although the authors have attempted to provide some formulations in Table 1, I still feel that these modules are far from sufficient to support the design of a workpiece. However, designing new constraints requires extreme caution and a significant amount of skill. Therefore, I am not particularly optimistic about this section. If the authors could propose a more universal paradigm for generating such constraints, many of my concerns would be alleviated.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents the framework of GINN, which formulates the objectives and constraints of geometry problem as the loss function to train the neural networks. More importantly, it proposes a diversity constraint, which avoids the mode-collapse of other generative models and promotes the model to generate diverse solutions for the geometry problem. In the experiment section, it validates the performance of GINN on four problems and additionally conducts an engineering design case study. It is able to find the accurate solution for the famous geometry problems, and produce diverse solutions for the engineering design problem.

### Strengths
- Although there have been a number of existing works using some similar losses to train their network, as mentioned in the related work, this paper presents the GINN framework with a very comprehensive summary and discussion on the common constraints used in the validation experiments. This would help the following works in formulating their own applications.
- Comparing to the physics-informed neural networks or the topology optimization, this paper proposes the diversity constraints for geometry problems. Comparing to other generative models such as boltzmann generators, the proposed diversity constraints help to avoid mode-collapse.

### Weaknesses
 - My main concern is about the technical novelty and the evaluation. Although this paper has presented many validation experiments, most of the results only show the performance of the GINN and some ablation settings, without comparing to other existing methods. In Section 4 it claims that there’s no established baselines, problems, and metrics for the data-free shape-generative modeling. Does it mean that there is no related work trying to solve the engineering design problem presented in Section 4.3??
- I understand that there are very much information to be presented in the paper. But it is a bit difficult to capture the key information. For example, the “topology” “smoothness” “surface sampling” are the defined metrics for each constraint? It’s better to have “constrained optimization”, “metrics”, “models” in bold font, and list all the metrics under the heading. The same problem exists in Section 4.3, there are too many headings to understand the structure of the writing.
- The generated solutions of the generative model seem not very satisfactory when compared to the figures in the papers [1,2]. The paper lacks a discussion on the quality of the generated results, which is crucial for evaluating the practical applicability of the proposed method.

### Questions
I’m not very familiar with the specific field (engineering design) of this paper. In my understanding, the idea of using objectives and constraints as loss functions is not completely new in the field of 3D generative models. But this paper has extended this idea with many more kinds of constraints and proposed the diversity constraint specifically for the engineering design problem. My only doubt is whether there are indeed no existing works to be compared with. I'd like to increase my rating if the authors can give more explanation on this.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes geometry-informed neural networks. The idea is to train a generative model not from data, but using objective function and constraints. Basically, the generative model is trained by a specification similar to an optimization problem.

### Strengths
The paper proposes an interesting idea that is worthy of further exploration. The research proposes the idea of a framework, but it does not demonstrate a working instantiation of the idea, so the research is only in its beginning stages. I think the concept is potentially very promising, but there are also predictable and significant obstacles that must be overcome. Design by optimization is a longstanding topic in many fields, but there are also many problems. Most notably, there aren't many or even any good examples of where optimization alone can give rise to interesting designs. Most of the time, this requires a good initialization that is already a design or the combination of user input (design) and optimization. For example, in architectural design you typically need an initial surface and you can design a pattern on the surface (e.g. a paneling). In furniture design, you also typically need to restrict the design space to a meaningful subset, e.g. by providing procedural rules or templates. At the moment, the method is an extension of an idea that does not have a working instantiation.

### Weaknesses
The major weakness of the paper is the lack of meaningful designs. Without interesting design examples, the paper is not meaningful. None of the designs shown in the paper are interesting and they cannot be recognized as mechanical, biological, architectural, ... objects. These are abstract designs like abstract art, and it is not meaningful to create art by optimization and then infer how this would transfer to engineering. I would suggest a three-step approach to tackling this problem:
1) The project should identify an example where a single interesting design can be created by optimization. This example should not be abstract but specific to an engineering problem and be recognizable as an intentional and meaningful design. This example can be generated by optimization alone. It doesn't matter if the design is from architecture, mechanical engineering, biology, geology, ... but it should be meaningful. If you want to go for something more discrete, I would recommend furniture or CAD designs. This may not work well with your framework, so I could imagine that free-form architecture could be a better application area, e.g. "Geodesic patterns", developable surfaces, self-supporting surfaces, or quad meshes.
2) The project should expand from this single design to generate a set of diverse designs by combining optimization with a diversity constraint.
3) The project should example from a set of designs generated by optimization to combining optimization with generative modeling.

The current submission does not have a demonstration of either 1, 2, or 3. Competing work (not cited) has at least somewhat of a demonstration of points 1 and 2 (e.g., "Fit and Diverse: Set Evolution for Inspiring 3D Shape Galleries"), but it would be desirable to have even better examples. 


It is possible to accept the paper for conceptual novelty, but I am not in favor of such a philosophy. A paper should introduce a conceptual novelty and at the same time introduce a working realization, not only the conceptual novelty. The conceptual novelty by itself should not be enough for publication. I conjecture that the reason why there aren't many other papers on this topic is because people could not find meaningful and working instantiations of this concept. There is an obvious approach: first generate a set of objects by optimization (e.g. furniture) and then train a generative model on this set. I am not aware of such a successful approach and a paper in this space should possibly demonstrate that it can beat such a baseline..

### Questions
N / A

### Soundness
2

### Presentation
2

### Contribution
2
