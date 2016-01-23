from random import randint

attribute_Values = [['Sunny','Cloudy','Rainy'],
					['Warm','Cold'],
					['Normal','High'],
					['Strong','Weak'],
					['Warm','Cool'],
					['Same','Change']
					]


def run_FindS_On_Given_Examples() :
	
	print 'Running Find-S on given examples'

	examples = [['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
				['Sunny','Warm','High','Strong','Warm','Same','Yes'],
				['Rainy','Cold','High','Strong','Warm','Change','No'],
				['Sunny','Warm','High','Strong','Cool','Change','Yes']
				]
	hypothesis = ['Phi','Phi','Phi','Phi','Phi','Phi']
	
	for instance in examples :
		hypothesis = run_FindS( instance, hypothesis )

	print 'Hypothesis for given examples = ', hypothesis


def run_FindS_On_Random_Examples() :

	print 'Running Find-S on random examples'

	target_Concept = ['Sunny','Warm','?','?','?','?']

	hypothesis = ['Phi','Phi','Phi','Phi','Phi','Phi']

	num_Examples = 0

	while hypothesis != target_Concept :

		random_Example = generate_Random_Example_From_Concept(target_Concept)

		print "Random Example = ", random_Example

		hypothesis = run_FindS(random_Example, hypothesis)

		num_Examples += 1

	print 'Number of Examples to reach target concept = ', num_Examples

	return num_Examples


def run_FindS_To_Calculate_Average_Number_Of_Examples() :

	sum = 0
	for i in range (1,21) :
		print 'Iteration number ',i
		sum = sum + run_FindS_On_Random_Examples()
	mean = sum/20
	print 'Average Number of Examples to reach target concept = ', mean

def generate_Random_Example_From_Concept( target_Concept ) :

	random_Example = []
	for attribute in attribute_Values :
		
		attribute_Index = randint(0, len(attribute)-1)
		random_Example.append(attribute[attribute_Index])
	
	random_Example.append( classify_Example_Using_Concept(target_Concept, random_Example) )

	return random_Example

def classify_Example_Using_Concept( concept, unclassified_Example ) :

	classification = 'Yes'
	for attribute_Value_Concept, attribute_Value_Instance in zip(concept, unclassified_Example) :
		
		if attribute_Value_Concept == '?' or attribute_Value_Instance in attribute_Value_Concept :
			continue
		elif attribute_Value_Concept == 'Phi' or not(attribute_Value_Instance in attribute_Value_Concept) :
			classification = 'No'
			break
	
	return classification


def run_FindS( instance, hypothesis ) :

	classification = classify_Example_Using_Concept( hypothesis, instance[0:-1])

	if (classification == 'Yes' and instance[-1] == 'Yes') or (classification == 'No' and instance[-1] == 'No'):
		return hypothesis

	elif classification == 'No' and instance[-1] == 'Yes':
		hypothesis = update_Hypothesis_For_Instance ( hypothesis, instance)
		print 'Updated Hypothesis = ',hypothesis
		return hypothesis

	elif classification == 'Yes' and instance[-1] == 'No':
		print 'Something\'s wrong.'
		
def update_Hypothesis_For_Instance( hypothesis, instance) :

	if 'Phi' in hypothesis:
		hypothesis = instance[0:-1]
		return hypothesis

	for attribute_Index, attribute_Value_Instance in enumerate(instance[0:-1]) :
		attribute_Value_Hypothesis = hypothesis[attribute_Index]
		if attribute_Value_Hypothesis == '?' or attribute_Value_Instance in attribute_Value_Hypothesis :
			continue
		elif not(attribute_Value_Instance in attribute_Value_Hypothesis) :
			
			if attribute_Value_Instance == 'Sunny' or attribute_Value_Instance == 'Cloudy' or attribute_Value_Instance == 'Rainy' :
				if not('_' in attribute_Value_Hypothesis) :
					hypothesis[attribute_Index] += '_' + attribute_Value_Instance
				else :
					hypothesis[attribute_Index] = '?'
			else :
				hypothesis[attribute_Index] = '?'
				
	return hypothesis


if __name__ == '__main__' :
	run_FindS_On_Given_Examples()
	run_FindS_On_Random_Examples()
	run_FindS_To_Calculate_Average_Number_Of_Examples()
