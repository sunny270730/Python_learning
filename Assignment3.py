#!/usr/bin/env python
# coding: utf-8

# In[1]:


###### assignment 2 #########

# 1) Fetch all Urls from the dict
# 2) Add new entity in flow_3
# 3) Update url in all flow
# 4) Delete the entity in flow_1   


flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

####   Fetch all Urls from the dict    ######

print(flow_1["api_data"]["url"], flow_2["api_data"]["url"],flow_3["api_data"]["url"]) 

##########   Add new entity in flow_3  ###########


flow_3["entities"].append({"entity": "price_range", "prompt": "Please enter your desired price range ?"}) 
print(flow_3)
#########    Update url in all flow    ##########

flow_1["api_data"]["url"] = "https://newurl.com/"     
flow_2["api_data"]["url"] = "https://newurl.com/"
flow_3["api_data"]["url"] = "https://newurl.com/"
print(flow_1["api_data"]["url"], flow_2["api_data"]["url"],flow_3["api_data"]["url"])

#########     Delete the entity in flow_1  ############

flow_1["entities"].remove({"entity": "product", "prompt": "can you please enter what are you searching ?"}) ###### delete entity###
print(flow_1)

      
      
      
      
      


# In[10]:


# Define the flows
flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    } 
}
class FlowManager:
    def __init__(self, flows):
        self.flows = flows
        
    def get_urls(self):
        urls = []
        for flow in self.flows:
            urls.append(flow['api_data']['url'])
        return urls
    
    def add_entity(self, flow_num, entity):
        self.flows[flow_num]['entities'].append(entity)
        
    def update_urls(self, new_url):
        for flow in self.flows:
            flow['api_data']['url'] = new_url
        
    def delete_entity(self, flow_num, entity_num):
        del self.flows[flow_num]['entities'][entity_num]
        
    def delete_entities(self, prompt):
        for flow in self.flows:
            entities = flow['entities']
            for i in range(len(entities)):
                if entities[i]['prompt'] == prompt:
                    del entities[i]
                    break 
# Create a FlowManager instance with the flows
fm = FlowManager([flow_1, flow_2, flow_3])

# # Task 1: Fetch all Urls from the dict
urls = fm.get_urls()
print("Urls: ", urls)

# Task 2: Add new entity in flow_3
new_entity = {"entity": "payment_method", "promt": "Please enter your flow ?"}
fm.add_entity(2, new_entity)
print('\n'"Flow 3 after adding new entity: ", flow_3)

# # Task 3: Update url in all flows
new_url = "https://newurl.freetyping.com/"
fm.update_urls(new_url)
print('\n'"Flows after updating urls: ", fm.flows)

# # Task 4: Delete the entity in flow_1
fm.delete_entity(0, 1)
print('\n'"Flow 1 after deleting entity: ", flow_1)

fm.delete_entities("Please enter your location ?")
print('\n'"Flows after deleting entities: ", fm.flows)


# In[14]:


x = [[10,15],[20,25]]
# print(type(x))
# y,z = x
# print("y",y)
# print("z",z)

for i,d in enumerate(x):
    if x[i] == d:
        x[i] = [40,45]

for d in x:
    print(d)


# In[11]:


# Define the flows
flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    } 
}

class FlowManager:
    def __init__(self, flows):
        self.flows = flows
        
    def get_urls(self):
        urls = []
        for flow in self.flows:
            urls.append(flow['api_data']['url'])
        return urls
    
    def add_entity(self, flow_num, entity):
        self.flows[flow_num]['entities'].append(entity)
        
    def update_urls(self, new_url):
        for flow in self.flows:
            flow['api_data']['url'] = new_url
        
    def delete_entity(self, flow_num, entity_num):
        del self.flows[flow_num]['entities'][entity_num]
        
    def delete_entities(self, prompt):
        for flow in self.flows:
            entities = flow['entities']
            for i in range(len(entities)):
                if entities[i]['prompt'] == prompt:
                    del entities[i]
                    break 
                    
# Create a FlowManager instance with the flows
fm = FlowManager([flow_1, flow_2, flow_3])

# Task 1: Fetch all Urls from the dict
urls = fm.get_urls()
print("Urls: ", urls)

# Task 2: Add new entity in flow_3
new_entity = {"entity": "payment_method", "prompt": "Please enter your payment method ?"}
fm.add_entity(2, new_entity)
print('\n'"Flow 3 after adding new entity: ", flow_3)

# Task 3: Update url in all flows
new_url = "https://newurl.freetyping.com/"
fm.update_urls(new_url)
print('\n'"Flows after updating urls: ", fm.flows)

# Task 4: Delete the entity in flow_1
fm.delete_entity(0, 1)
print('\n'"Flow 1 after deleting entity: ", flow_1)

# Task 5: Delete entities with prompt "Please enter your location ?"
fm.delete_entities("Please enter your location ?")
print('\n'"Flows after deleting entities: ", fm.flows)


# In[ ]:




