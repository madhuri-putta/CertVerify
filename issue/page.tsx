"use client";
import { useState } from 'react';
import Navbar from '@/components/Navbar';

export default function IssueCertificate() {
    const [formData, setFormData] = useState({
        student_id: '',
        student_name: '',
        course: '',
        institute: '',
        year: '',
        issuer_email: ''
    });

    const [file, setFile] = useState<File | null>(null);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!file) {
            alert("Please upload the certificate image to register its hash!");
            return;
        }

        const data = new FormData();
        data.append('file', file);
        Object.keys(formData).forEach(key => {
            data.append(key, formData[key as keyof typeof formData]);
        });

        try {
            const res = await fetch('http://localhost:8000/api/issue', {
                method: 'POST',
                body: data,
            });
            const result = await res.json();
            if (res.ok) {
                alert(`Certificate Issued! Hash: ${result.hash}`);
            } else {
                alert('Failed to issue certificate');
            }
        } catch (err) {
            console.error(err);
            alert('Error issuing certificate');
        }
    };

    return (
        <div className="min-h-screen text-white pt-20">
            <Navbar />
            <div className="max-w-2xl mx-auto p-6 bg-gray-800/60 backdrop-blur-md rounded-xl shadow-lg border border-gray-700 mt-10">
                <h1 className="text-2xl font-bold mb-6 text-blue-400">Issue New Certificate</h1>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Student ID</label>
                        <input type="text" name="student_id" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Student Name</label>
                        <input type="text" name="student_name" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Course</label>
                        <input type="text" name="course" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Institute</label>
                        <input type="text" name="institute" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Year</label>
                        <input type="text" name="year" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-300">Issuer Email</label>
                        <input type="email" name="issuer_email" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" required />
                    </div>
                    <div className="bg-gray-700/50 p-4 rounded border border-gray-600">
                        <label className="block text-sm font-medium text-blue-300 mb-2">Certificate Image (Required for Verification)</label>
                        <p className="text-xs text-gray-400 mb-2">Upload the exact image file you want to issue. This registers its digital signature.</p>
                        <input type="file" onChange={handleFileChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white" accept="image/*" required />
                    </div>
                    <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition">
                        Generate & Issue Certificate
                    </button>
                </form>
            </div>
        </div>
    );
}
