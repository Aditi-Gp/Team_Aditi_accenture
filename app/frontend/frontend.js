import { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Loader2 } from 'lucide-react';

export default function App() {
  const [productId, setProductId] = useState('4277');
  const [storeId, setStoreId] = useState('48');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/orchestrate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          product_id: parseInt(productId),
          store_id: parseInt(storeId),
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error('Failed to fetch orchestration results', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 md:p-10">
      <h1 className="text-3xl font-bold mb-6 text-center">🧠 Multi-Agent Retail Optimizer</h1>
      <Card className="max-w-xl mx-auto p-4 shadow-xl">
        <CardContent>
          <div className="space-y-4">
            <div>
              <Label>Product ID</Label>
              <Input value={productId} onChange={(e) => setProductId(e.target.value)} />
            </div>
            <div>
              <Label>Store ID</Label>
              <Input value={storeId} onChange={(e) => setStoreId(e.target.value)} />
            </div>
            <Button className="w-full" onClick={handleSubmit} disabled={loading}>
              {loading ? <Loader2 className="animate-spin mr-2" /> : 'Run Analysis'}
            </Button>
            {result && (
              <div className="space-y-4 mt-6">
                <Card>
                  <CardContent className="p-4">
                    <h2 className="font-semibold text-lg">Demand Forecast</h2>
                    <p>{result.demand_prediction}</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <h2 className="font-semibold text-lg">Inventory Status</h2>
                    <p>{result.inventory_status}</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <h2 className="font-semibold text-lg">Customer Info</h2>
                    <p>{result.customer_info}</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <h2 className="font-semibold text-lg">Pricing Suggestion</h2>
                    <p>{result.price_recommendation}</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <h2 className="font-semibold text-lg">LLM Summary</h2>
                    <Textarea className="bg-white" value={result.llm_summary} readOnly rows={6} />
                  </CardContent>
                </Card>
              </div>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
