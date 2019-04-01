import nsepy

msg = "Hello World"
i=10
print(msg)
#Stock history
sbin = get_history(symbol='SBIN',
                    start=date(2015,1,1), 
                    end=date(2015,1,10))
sbin[[ 'VWAP', 'Turnover']].plot(secondary_y='Turnover')
print (sbin)

