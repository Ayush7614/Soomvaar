# shipping-cost-prediction
Shipping Cost Predition for Logistics based Use Case


### Project Code - (.ipynb format)


### ***Description***


In land transport, dispatchers receive orders of shipments and find suitable carriers. This is a
process that relies almost entirely on human decisions and interactions. The dispatcher has
some tools to access a list of available carriers, and contacts them until he finds someone with
whom he agrees on a price. When the price is agreed, the carrier takes the responsibility of
delivering the given shipment from the origin to the destination.

It is easy to imagine that deciding the price for a shipment is not an easy task, given the number
of human factors that enter into play. For this reason, it is desirable to build a tool able to
predict a price that the dispatchers can use as a guideline. 

### ***Task Implementation***
• An ensemble model is trained using the train data contained in train_data.csv and compute cost
predictions for the cases contained in test_data.csv. 


The evaluation of the quality of predictions against the true values, using the $R^2$ (coefficient of determination) metric.

Readability factor is stressed during coding along with good evaluation metric.

### ***Glimplse of Visualization***

* **Box-plot to visualize outliers of Feature-weight**


![image](/images/graph-barplot-histogram-weight.jpg)


* **Box-plot to visualize outliers of Feature-cost**


![image](/images/graph-boxplot-cost.jpg)

* **Feature Importance**


![image](/images/feature_importance_Ada_Boost.jpg)




