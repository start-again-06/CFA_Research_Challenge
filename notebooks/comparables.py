import pandas as pd
peer_data = pd.DataFrame({
    "Company":["Peer1","Peer2","Peer3","Peer4"],
    "PE":[18,20,22,19],
    "EV_EBITDA":[12,14,13,11]
})
peer_data
avg_pe = peer_data["PE"].mean()
avg_ev_ebitda = peer_data["EV_EBITDA"].mean()
print("Average PE:",avg_pe)
print("Average EV/EBITDA:",avg_ev_ebitda)
company_eps = 2.5
target_price = avg_pe * company_eps
print("Comparable Valuation Target Price:",target_price)
